import logging


def generate_invitations(template, attendees):
    """
    Generates personalized invitation files from a template and a list of attendees.

    Args:
        template (str): The template with placeholders for name, event_title, event_date, and event_location.
        attendees (list[dict]): List of dictionaries containing attendee information.

    Returns:
        None: Creates output files named output_X.txt (X is the index of the attendee).

    """
    if not isinstance(template, str):
        logging.error("Invalid input type: template must be a string.")
        sys.exit()

    if not isinstance(attendees, list) and all(isinstance(att, dict) for att in attendees):
        logging.error("Invalid input type: attendees must be a list of dictionaries.")
        sys.exit()

    if not template.strip():
        logging.error("Template is empty, no output files generated.")
        sys.exit()

    if not attendees:
        logging.error("No data provided, no output files generated.")
        sys.exit()

    # Process each attendee
    for i, attendee in enumerate(attendees, start=1):
        processed_template = template.format(
            name=attendee.get("name", "N/A"),
            event_title=attendee.get("event_title", "N/A"),
            event_date=attendee.get("event_date", "N/A"),
            event_location=attendee.get("event_location", "N/A")
        )

        output_filename = f"output_{i}.txt"
        with open(output_filename, "w") as output_file:
            output_file.write(processed_template)

        print(f"Invitation for {attendee['name']} saved to {output_filename}")
