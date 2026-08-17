

        # Start new session
        manager.start_session(current_window)


    # =====================================
    # 8 HOUR REPORT CHECK
    # =====================================

    if datetime.now() >= next_report_time:

        print("Generating 8-hour report...")


        # Generate Excel + PDF report
        generate_report()


        # Schedule next report
        next_report_time = report_start_time + timedelta(minutes=2)

        print("Next report scheduled after 8 hours")


    # =====================================
    # CHECK EVERY 2 SECONDS
    # =====================================

        time.sleep(2)