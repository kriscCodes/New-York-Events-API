# New York Events API

The New York Events API is a Flask-based application that serves as a platform for managing and accessing information about various events happening in New York City. This API allows users to create, retrieve, and manage event details efficiently.

## Features
- **Event Creation**: Users can add new events via a form submission.
- **Event Retrieval**: Allows fetching details of a specific event by name or listing all events.
- **Data Storage**: Utilizes SQLite database with SQLAlchemy for storing event details.
- **Cross-Origin Resource Sharing (CORS)**: Enabled to allow safe cross-origin requests in a web application context.

## API Endpoints
- `POST /form`: Add a new event.
- `GET /get-all-events`: List all available events.
- `GET /get-event-id/<id>`: Retrieve details of a specific event.
- `GET /get-event/<event_name>`: Retrieve details of a specific event.


## How to Use
- Access the documentation for creating and reading events, visit `https://new-york-events-66105853a688.herokuapp.com/`.

## Future Plans
- **More Endpoints**: There aren't as many endpoints as I would like due to time restraints but I will be adding more soon.
- **Put and Delete entries**: I want for entries to be updated and potentially deleted.
- **Specificty**: I want the form to have specific requirements that way it's easier to use and interact with the data when consuming this API or adding any entry.

## Contributing
Contributions to the New York Events API are welcome.
