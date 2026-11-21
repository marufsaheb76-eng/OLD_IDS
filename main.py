import threading
import time

import ui
import engine

running = False
worker = None

stats = {
    "total": 0,
    "completed": 0,
    "success": 0,
    "failed": 0
}


def progress(completed, total, success, failed):
    stats.update({
        "total": total,
        "completed": completed,
        "success": success,
        "failed": failed
    })


def backup():
    global running

    visual_stop = threading.Event()

    visual_thread = threading.Thread(
        target=ui.run_visual_effect,
        args=(visual_stop,),
        daemon=True
    )

    visual_thread.start()

    try:
        result = engine.start_backup(progress)

        stats.update({
            "total": result["total"],
            "completed": (
                result["success"]
                + result["failed"]
                + result["stopped"]
            ),
            "success": result["success"],
            "failed": result["failed"]
        })

    except Exception:
        pass

    finally:
        visual_stop.set()
        running = False


def main():
    global running, worker

    while True:
        choice = ui.menu()

        if choice == "1":

            if not running:
                running = True

                worker = threading.Thread(
                    target=backup,
                    daemon=True
                )

                worker.start()

            ui.pause()

        elif choice == "2":

            if running:
                engine.stop_backup()

            ui.pause()

        elif choice == "3":

            ui.clear()
            ui.banner()

            print(f"Status: {'RUNNING' if running else 'IDLE'}")
            print(f"Total: {stats['total']}")
            print(f"Completed: {stats['completed']}")
            print(f"Uploaded: {stats['success']}")
            print(f"Failed: {stats['failed']}")

            ui.pause()

        elif choice == "4":

            if running:
                engine.stop_backup()
                ui.pause()
            else:
                break

        else:
            time.sleep(1)


if __name__ == "__main__":
    main()
