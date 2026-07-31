from database import get_all_activity

activities = get_all_activity()

print("=" * 50)
print("Today's Activity")
print("=" * 50)

for activity in activities:
    print(activity)