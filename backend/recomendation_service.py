import random

NORMAL_RECOMMENDATIONS = [
    "Maintain a consistent sleep schedule every day.",
    "Engage in light physical exercise for at least 30 minutes several times a week.",
    "Keep a healthy balance between work, study, and rest.",
    "Make time for activities that you enjoy.",
    "Maintain positive relationships with friends and family.",
    "Eat nutritious meals and stay hydrated.",
    "Continue practicing habits that support your mental well-being.",
    "Set realistic and achievable daily goals.",
    "Take time for relaxation and self-reflection.",
    "Maintain routines that support your physical and emotional wellness."
]

STRESS_RECOMMENDATIONS = [
    "Practice deep breathing exercises for a few minutes each day.",
    "Break large tasks into smaller and more manageable steps.",
    "Take regular breaks during work or study sessions.",
    "Reduce multitasking to improve focus and lower mental strain.",
    "Engage in light physical activities such as walking or stretching.",
    "Limit caffeine intake if it increases feelings of tension or stress.",
    "Keep a journal to record thoughts and stressors.",
    "Prioritize the most important tasks first.",
    "Spend time on hobbies or activities that help you relax.",
    "Consider talking with friends or family about the pressures you are experiencing."
]

DEPRESSION_RECOMMENDATIONS = [
    "Try to maintain a daily routine, even with small activities.",
    "Set simple and achievable goals for each day.",
    "Spend some time outdoors and get natural sunlight.",
    "Stay connected with people who can provide support.",
    "Consider seeking professional help if your feelings persist or worsen.",
    "Focus on one positive activity at a time.",
    "Make sure your basic needs, such as eating and sleeping, are met.",
    "Avoid isolating yourself for long periods.",
    "Keep track of small accomplishments each day.",
    "Give yourself time and space for recovery and self-care."
]

ANXIETY_RECOMMENDATIONS = [
    "Practice grounding techniques to help focus on the present moment.",
    "Use slow and controlled breathing exercises when feeling anxious.",
    "Reduce exposure to information that triggers excessive worry.",
    "Focus on what you can control and let go of what you cannot.",
    "Engage in light physical activity to reduce tension.",
    "Try mindfulness or meditation for a few minutes each day.",
    "Ensure you get enough rest and sleep.",
    "Write down anxious thoughts to better understand and manage them.",
    "Avoid making important decisions when anxiety levels are high.",
    "Consider speaking with a mental health professional if anxiety frequently affects your daily life."
]


def get_random_recommendation(category: str):
    recommendations = {
        "Normal": NORMAL_RECOMMENDATIONS,
        "Stress": STRESS_RECOMMENDATIONS,
        "Depression": DEPRESSION_RECOMMENDATIONS,
        "Anxiety": ANXIETY_RECOMMENDATIONS,
    }

    return random.choice(
        recommendations.get(
            category,
            NORMAL_RECOMMENDATIONS
        )
    )