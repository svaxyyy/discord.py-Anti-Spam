# discord.py-Anti-Spam
This is not the full customized module! For Questions dm Svaxyy#0859 on discord. This code warns a guy if he spams 5 messages and on 8 warings he is getting kicked

# Please leave a reaction on Discord that would be nice!
- ✅ / 🆗

# Module based!
 This Project is only to show guys the project with a code example which is more expanded than the preview of the module!
 
 # Module Options:
 
     DEFAULTS:
        warn_threshold: 3
            This is the amount of duplicates that result in a warning within the message_interval

        kick_threshold: 2
            This is the amount of warns required before a kick is the next punishment

        ban_threshold: 2
            This is the amount of kicks required before a ban is the next punishment

        message_interval: 30000ms (30 Seconds)
            Amount of time a message is kept before being discarded. Essentially the amount of time (In milliseconds) a message can count towards spam

        guild_warn_message: "Hey $MENTIONUSER, please stop spamming/sending duplicate messages."
            The message to be sent in the guild upon warn_threshold being reached

        guild_kick_message: "$USERNAME was kicked for spamming/sending duplicate messages."
            The message to be sent in the guild upon kick_threshold being reached

        guild_ban_message: "$USERNAME was banned for spamming/sending duplicate messages."
            The message to be sent in the guild upon ban_threshold being reached

        user_kick_message : "Hey $MENTIONUSER, you are being kicked from $GUILDNAME for spamming/sending duplicate messages."
            The message to be sent to the user who is being warned

        user_ban_message : "Hey $MENTIONUSER, you are being banned from $GUILDNAME for spamming/sending duplicate messages."
            The message to be sent to the user who is being banned

        user_failed_kick_message : "I failed to punish you because I lack permissions, but still you shouldn't spam"
            The message to be sent to the user if the bot fails to kick them

        user_failed_ban_message : "I failed to punish you because I lack permissions, but still you shouldn't spam"
            The message to be sent to the user if the bot fails to ban them

        message_duplicate_count: 5
            The amount of duplicate messages needed within message_interval to trigger a punishment

        message_duplicate_accuracy: 90
            How 'close' messages need to be to be registered as duplicates (Out of 100)

        delete_spam: True
            Whether or not to delete messages marked as spam

            *Won't delete messages if* ``no_punish`` *is* ``True``

        ignore_perms: [8]
            The perms (ID Form), that bypass anti-spam

            **Not Implemented**

        ignore_users: []
            The users (ID Form), that bypass anti-spam

        ignore_channels: []
            Channels (ID Form), that bypass anti-spam

        ignore_roles: []
            The roles (ID Form), that bypass anti-spam

        ignore_guilds: []
            Guilds (ID Form), that bypass anti-spam

        ignore_bots: True
            Should bots bypass anti-spam?

        warn_only: False
            Whether or not to only warn users,
            this means it will not kick or ban them

        no_punish: False
            Don't punish anyone, simply return
            whether or not they should be punished
            within propagate.
            This essentially lets the end user
            handle punishments themselves.

            To check if someone should be punished, use the returned
            value from the ``propagate`` method. If should_be_punished_this_message
            is True then this package believes they should be punished.
            Otherwise just ignore that message since it shouldn't be punished.

        per_channel_spam: False
            Track spam as per channel,
            rather then per guild.

        guild_warn_message_delete_after: None
            The time to delete the ``guild_warn_message`` message

        user_kick_message_delete_after: None
            The time to delete the ``user_kick_message`` message

        guild_kick_message_delete_after: None
            The time to delete the ``guild_kick_message`` message

        user_ban_message_delete_after: None
            The time to delete the ``user_ban_message`` message

        guild_ban_message_delete_after: None
            The time to delete the ``guild_ban_message`` message

        delete_zero_width_chars: True
            Should zero width characters be removed from messages
            
            
# Module link:
https://pypi.org/project/Discord-Anti-Spam/
  
