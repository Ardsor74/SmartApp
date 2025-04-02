from calendar_app import print_calendar, add_event, remove_event, print_events, save_events, load_events
from expenses_app import add_expense, print_expenses, save_expenses, load_expenses
from automation_app import send_notification, send_sms
from ai_news_updater import get_sports_news, update_website
from datetime import datetime

if __name__ == "__main__":
    now = datetime.now()
    print("Calendar:")
    print_calendar(now.year, now.month)

    events = load_events()
    add_event(events, now.strftime("%Y-%m-%d"), "Today's event")
    remove_event(events, "2025-04-03", "Doctor's appointment")
    print("\nEvents:")
    print_events(events)
    save_events(events)

    print("\nExpenses:")
    expenses = load_expenses()
    add_expense(expenses, "Coffee", 2.50, "Food")
    add_expense(expenses, "Lunch", 10.00, "Food")
    add_expense(expenses, "Uber", 15.00, "Transport")
    print_expenses(expenses)
    save_expenses(expenses)

    print("\nSending Notification...")
    send_notification("This is a test notification!")
    send_sms("This is a test SMS!", "+1234567890", "+0987654321")

    print("\nUpdating Website with Sports News...")
    news = get_sports_news()
    update_website(news)
    print("Website updated with the latest sports news!")