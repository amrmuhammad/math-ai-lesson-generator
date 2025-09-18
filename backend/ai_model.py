def generate_lesson(topic):
    """
    Dummy AI lesson generator.
    Replace with actual AI model or API integration.
    """
    if "quadratic" in topic.lower():
        lesson = (
            "### Quadratic Equations\n"
            "A quadratic equation has the form $ax^2 + bx + c = 0$.<br>"
            "The solutions are given by the quadratic formula:<br>"
            "$$x = \\frac{-b \\pm \\sqrt{b^2 - 4ac}}{2a}$$"
        )
        latex_list = [
            "ax^2 + bx + c = 0",
            "x = \\frac{-b \\pm \\sqrt{b^2 - 4ac}}{2a}"
        ]
    else:
        lesson = f"### {topic.title()}\nThis is a placeholder lesson for **{topic}**. Replace this with real AI-powered content!"
        latex_list = []
    return lesson, latex_list
