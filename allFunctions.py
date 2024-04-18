functions = [
        #Weather Functions
        {
            "name": "current_weather",
            "description": "Get the current weather in a given city and state. Use fahrenheit for all temperatures",
            "parameters": {
                "type": "object",
                "properties": {
                    "firstArg": {
                        "type": "string",
                        "description": "The city and state e.g. Katy Texas",
                    }
                    }
                },
                "required": ["firstArg"],
            },
            {
            "name": "weather_forecast",
            "description": "Get the current weather forecast in a given city and state for however many days. Use fahrenheit for all temperatures",
            "parameters": {
                "type": "object",
                "properties": {
                    "firstArg": {
                        "type": "string",
                        "description": "The city and state along with The amount of days to forecast e.g. Katy Texas 5",
                    }
                    }
                },
                "required": ["firstArg"]
            },
            {
            "name": "moon_phase",
            "description": "Get the current moon phase in a given city and state.",
            "parameters": {
                "type": "object",
                "properties": {
                    "firstArg": {
                        "type": "string",
                        "description": "The city and state for the moon phase e.g. Katy Texas",
                    }
                    }
                }
            },
        #Calendar Functions
            {
            "name": "list_events",
            "description": "Get the current events for today until the day specified",
            "parameters": {
                "type": "object",
                "properties": {
                    "firstArg": {
                        "type": "integer",
                        "description": "The number of days in the future to look for events.",
                    }
                    }
                },
                
            },
        #Map Functions
            {
            "name": "search_map_by_name",
            "description": "Search the places in the area by the given name",
            "parameters": {
                "type": "object",
                "properties": {
                    "firstArg": {
                        "type": "string",
                        "description": "The name to search for in the area",
                    }
                    }
                },
                "required": ["firstArg"],
            },
        #Data Functions
            {
            "name": "search_data",
            "description": "search for any file by name. Use this functions for any inquiries regarding external files e.g. summarize, give tips",
            "parameters": {
                "type": "object",
                "properties": {
                    "firstArg": {
                        "type": "string",
                        "description": "The title of the file to search for",
                    }
                    }
                },
                "required": ["firstArg"],
            },
        #App Functions
            # {
            # "name": "open_app",
            # "description": "Open any app or apps on computer by name",
            # "parameters": {
            #     "type": "object",
            #     "properties": {
            #         "firstArg": {
            #             "type": "string",
            #             "description": "The name of the app to open",
            #         }
            #         }
            #     },
            #     "required": ["firstArg"],
            # },
            # {
            # "name": "close_app",
            # "description": "Close any app or apps on computer by name",
            # "parameters": {
            #     "type": "object",
            #     "properties": {
            #         "firstArg": {
            #             "type": "string",
            #             "description": "The name of the app to close e.g. close phone => closes phone app",
            #         }
            #         }
            #     },
            #     "required": ["firstArg"],
            # },
        #Music Functions
            {
            "name": "pause_track",
            "description": "pause the currently playing track",
            "parameters": {
                "type": "object",
                "properties": {
                    "firstArg": {
                        "type": "string",
                        "description": "Empty argument to avoid error",
                    }
                    }
                },
            },
            {
            "name": "play_track",
            "description": "resume the currently playing track",
            "parameters": {
                "type": "object",
                "properties": {
                    "firstArg": {
                        "type": "string",
                        "description": "Empty argument to avoid error",
                    }
                    }
                },
            },
            {
            "name": "next_track",
            "description": "go to next track",
            "parameters": {
                "type": "object",
                "properties": {
                    "firstArg": {
                        "type": "string",
                        "description": "Empty argument to avoid error",
                    }
                    }
                },
            },
            {
            "name": "previous_track",
            "description": "go to previous track",
            "parameters": {
                "type": "object",
                "properties": {
                    "firstArg": {
                        "type": "string",
                        "description": "Empty argument to avoid error",
                    }
                    }
                },
            },
            {
            "name": "restart_track",
            "description": "restarts current track",
            "parameters": {
                "type": "object",
                "properties": {
                    "firstArg": {
                        "type": "string",
                        "description": "Empty argument to avoid error",
                    }
                    }
                },
            },
            {
            "name": "current_track",
            "description": "get info for the currently playing track/song e.g. what is the name of the current song, current song",
            "parameters": {
                "type": "object",
                "properties": {
                    "firstArg": {
                        "type": "string",
                        "description": "Empty argument to avoid error",
                    }
                    }
                },
            },
            {
            "name": "like_track",
            "description": "likes the current track playing",
            "parameters": {
                "type": "object",
                "properties": {
                    "firstArg": {
                        "type": "string",
                        "description": "Empty argument to avoid error",
                    }
                    }
                },
            },
            {
            "name": "dislike_track",
            "description": "dislikes the current track playing",
            "parameters": {
                "type": "object",
                "properties": {
                    "firstArg": {
                        "type": "string",
                        "description": "Empty argument to avoid error",
                    }
                    }
                },
            },
            {
            "name": "search_track",
            "description": "searches for a specific song and plays it",
            "parameters": {
                "type": "object",
                "properties": {
                    "firstArg": {
                        "type": "string",
                        "description": "the song to search for e.g. upside down jack johnson",
                    }
                    }
                },
                "required": ["firstArg"],
            },
            {
            "name": "search_playlist",
            "description": "searches for a specific playlist and plays it",
            "parameters": {
                "type": "object",
                "properties": {
                    "firstArg": {
                        "type": "string",
                        "description": "the playlist to search for e.g. christmas music",
                    }
                    }
                },
                "required": ["firstArg"],
            },
            {
            "name": "toggle_shuffle",
            "description": "toggles shuffle for playback",
            "parameters": {
                "type": "object",
                "properties": {
                    "firstArg": {
                        "type": "string",
                        "description": "Empty argument to avoid error",
                    }
                    }
                },
            },
            {
            "name": "toggle_repeat",
            "description": "toggles repeat for playback",
            "parameters": {
                "type": "object",
                "properties": {
                    "firstArg": {
                        "type": "string",
                        "description": "Empty argument to avoid error",
                    }
                    }
                },
            },
            {
            "name": "set_track_volume",
            "description": "set the volume for the current track",
            "parameters": {
                "type": "object",
                "properties": {
                    "firstArg": {
                        "type": "integer",
                        "description": "the number to set the volume to. has to be from 0-100",
                    }
                    }
                },
            },
            {
            "name": "start_music",
            "description": "starts music on specified device if music is already playing it will transfer the music instead",
            "parameters": {
                "type": "object",
                "properties": {
                    "firstArg": {
                        "type": "string",
                        "description": "the device to transfer music to. set to pc if not specified",
                    }
                    }
                },
                "required": ["firstArg"],
            },
        #Clock Functions
            {
            "name": "current_time",
            "description": "states the current time in current timezone",
            "parameters": {
                "type": "object",
                "properties": {
                    "firstArg": {
                        "type": "string",
                        "description": "",
                    }
                    }
                },
            },
            {
            "name": "set_timer",
            "description": "sets a timer for specified time in seconds e.g. 2 minutes = 120 seconds",
            "parameters": {
                "type": "object",
                "properties": {
                    "firstArg": {
                        "type": "string",
                        "description": "amount of time to set timer for and what the timer is for",
                    }
                    }
                },
            },
            
    ]
