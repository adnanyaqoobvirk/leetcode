from enum import StrEnum, auto

class MessageType(StrEnum):
    OFFLINE = "OFFLINE"
    MESSAGE = "MESSAGE"

class Solution:
    OFFLINE_EXPIRY_MINUTES = 60

    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        def updateAllUsers():
            for i in range(numberOfUsers):
                user_mentions[i] += 1

        def updateOnlineUsers():
            for user_id in online_users:
                user_mentions[user_id] += 1
        
        def updateMentionedUsers():
            user_ids = mention_string.split(" ")
            for user_id in user_ids:
                user_mentions[int(user_id[2:])] += 1

        events.sort(key=lambda x: x[0], reverse=True)
        events.sort(key=lambda x: int(x[1]))

        online_users = set(range(numberOfUsers))
        offline_users = deque()
        user_mentions = [0] * numberOfUsers

        for message_type, timestamp, mention_string in events:
            t = int(timestamp)
            while offline_users and offline_users[0][1] <= t:
                user_id, _ = offline_users.popleft()
                online_users.add(user_id)

            if message_type == MessageType.MESSAGE:
                if mention_string == "ALL":
                    updateAllUsers()
                elif mention_string == "HERE":
                    updateOnlineUsers()
                else:
                    updateMentionedUsers()
            else:
                user_id = int(mention_string)
                online_users.remove(user_id)
                offline_users.append((
                    user_id, 
                    int(timestamp) + self.OFFLINE_EXPIRY_MINUTES
                    )
                )
        
        return user_mentions