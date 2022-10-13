### JSON file format:
````json
{
    "history_link":"<link to history website>",
    "anime_link":"<link to anime website>",
    "games_link":"<link to games website>",
    "history": [
        {
            "title":"string",
            "description":"string",
	        "date":"dateTime",
            "cv_images":"string <location of file in github>",
            "images": []
	    },
        {
            "title":"string",
            "description":"string",
	        "date":"dateTime",
            "cv_images":"string <location of file in github>",
            "images": []
	    }
    ],

    "anime": [
        {
            "title":"string",
            "description":"string",
            "release_date":"dateTime",
            "cv_images":"string <location of file in github>", 
            "images": [],
            "genre":"string"
        },
        {
            "title":"string",
            "description":"string",
            "release_date":"dateTime",
            "cv_images":"string <location of file in github>", 
            "images": [],
            "genre":"string"
        }
    ],

    "game": [
        {
            "title":"string",
            "description":"string",
            "release_date":"dateTime",
            "cv_images":"string <location of file in github>",
            "images": [],
            "genre":"string"
        },
        {
            "title":"string",
            "description":"string",
            "release_date":"dateTime",
            "cv_images":"string <location of file in github>",
            "images": [],
            "genre":"string"
        }
    ]
}
````
