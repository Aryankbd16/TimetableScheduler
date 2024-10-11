from django import template

register = template.Library()

@register.simple_tag(takes_context=True)
def sub(context, schedule, section_id, week_day, time_slot):
    try:
        # Access the class information based on the provided arguments
        class_data = schedule.get_class_by_section_id_day_time(section_id, week_day, time_slot)

        # Format the class information for display
        formatted_data = f"{class_data.course.course_name}<br>{class_data.instructor.name}"

        return formatted_data
    except (AttributeError, KeyError):
        # Handle cases where data might be missing or invalid
        return "No class scheduled"