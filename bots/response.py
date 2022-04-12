welcome_msg = """{
    "type": "AdaptiveCard",
    "body": [
        {
            "type": "TextBlock",
            "size": "Medium",
            "weight": "Bolder",
            "text": "${title}"
        },
        {
            "type": "TextBlock",
            "text": "${description}",
            "wrap": true
        },
        {
            "type": "TextBlock",
            "wrap": true,
            "text": "write to us at **support@trio.com** for any query or concern."
        }
    ],
    "actions": [
        {
            "type": "Action.OpenUrl",
            "url": "${viewUrl}",
            "title": "Opt In for Data Sharing "
        }
    ],
    "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
    "version": "1.3"
}
"""

welcome_json="""{
    "title": "Welcome to Trio Bot",
    "description":"I am here to help you. You can always say **Hi** to start interacting with me. I can provide you with assistance in improving your work efficiency, habbits and your health. You can also log your working times directly. I would be notifying you regularly to provide you methods to stay healthy, focussed and keep you posted with the new events occuring in the organisation. **You can also opt in or opt out of Health monitoring facility to maintain your privacy with your employer by single click**",
    "creator": {
        "name": "Matt Hidinger",
        "profileImage": "https://pbs.twimg.com/profile_images/3647943215/d7f12830b3c17a5a9e4afcc370e3a37e_400x400.jpeg"
    },
    "createdUtc": "2017-02-14T06:08:39Z",
    "viewUrl": "https://adaptivecards.io",
    "properties": [
        {
            "key": "Board",
            "value": "Adaptive Cards"
        },
        {
            "key": "List",
            "value": "Backlog"
        },
        {
            "key": "Assigned to",
            "value": "Matt Hidinger"
        },
        {
            "key": "Due date",
            "value": "Not set"
        }
    ]
}"""

optin_msg ="""{
    "type": "AdaptiveCard",
    "body": [
        {
            "type": "TextBlock",
            "wrap": true,
            "text": "Thanks for sharing your information with us.  \nYou can always opt out  to maintain your data privacy. "
        }
    ],
    "actions": [
        {
            "type": "Action.OpenUrl",
            "url": "${viewUrl}",
            "title": "Opt Out of Data Sharing "
        }
    ],
    "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
    "version": "1.3"
}"""

drink_water = """{
    "type": "AdaptiveCard",
    "body": [
        {
            "type": "TextBlock",
            "wrap": true,
            "text": "Its time for you to take a 5 minutes break to refresh your mind and body. Go for it! **Keep calm and drink water.**"
        }
    ],
    "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
    "version": "1.3"
}"""

feel_sick = """{
    "type": "AdaptiveCard",
    "body": [
        {
            "type": "TextBlock",
            "wrap": true,
            "text": "Seems like you are not feeling well. Is that the case? let us know if you need to take care of yourself today."
        }
    ],
    "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
    "version": "1.3",
    "actions": [
        {
            "type": "Action.Submit",
            "title": "Need Sick leave?"
        }
    ]
}"""


prod_hack="""{
    "type": "AdaptiveCard",
    "body": [
        {
            "type": "TextBlock",
            "size": "Medium",
            "weight": "Bolder",
            "text": "${title}"
        },
        {
            "type": "TextBlock",
            "wrap": true,
            "text": "**Stop Multitasking**\n\nIt's a productivity killer. Research shows that productivity can be reduced by as much as 40% by the mental blocks created when people switch tasks. Even more startling, in a University of London study, IQ dropped 15 points for some multitasking men.\n\nNeed more evidence? A study out of the University of Sussex in the UK indicates that multitasking may actually be physically harming your brain. The study found that participants addicted to using multiple devices simultaneously had a lower gray-matter density in a brain area called the anterior cingulate cortex, which is linked to emotional control and decision-making, empathy, and the brain's response to rewards.\n\nSo stop trying to do everything at once. Instead, dramatically increase productivity by giving your full attention to one task at a time. When your eyes and hands start drifting toward something else, think about how important it is to keep all your little gray cells."
        }
    ],
    "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
    "version": "1.3"
}
"""