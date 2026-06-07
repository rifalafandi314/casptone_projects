from ml_service import predict_all_conditions
from nlp_service import predict_text
from recomendation_service import get_random_recommendation


def generate_final_assessment(
    questionnaire_result,
    text_result
):

    stress = questionnaire_result["stress"]["prediction"]
    anxiety = questionnaire_result["anxiety"]["prediction"]
    depression = questionnaire_result["depression"]["prediction"]

    text_prediction = text_result["prediction"]

    # HIGH STRESS
    if (
        "High" in stress
        and text_prediction == "Stress"
    ):
        return "High Stress Risk"

    # HIGH ANXIETY
    if (
        "Severe" in anxiety
        and text_prediction == "Anxiety"
    ):
        return "High Anxiety Risk"

    # HIGH DEPRESSION
    if (
        "Severe" in depression
        and text_prediction == "Depression"
    ):
        return "High Depression Risk"

    # MODERATE
    if (
        "Moderate" in stress
        or "Moderate" in anxiety
        or "Moderate" in depression
    ):
        return "Moderate Risk"

    return "Low Risk"


def get_recommendation_category(
    final_assessment,
    text_prediction
):
    """
    Menentukan kategori rekomendasi.
    """

    if final_assessment == "High Anxiety Risk":
        return "Anxiety"

    if final_assessment == "High Depression Risk":
        return "Depression"

    if final_assessment == "High Stress Risk":
        return "Stress"

    if final_assessment == "Moderate Risk":
        return text_prediction

    return "Normal"


def predict_combined(data: dict):

    questionnaire_result = predict_all_conditions(data)

    text_result = predict_text(
        data["text"]
    )

    final_assessment = generate_final_assessment(
        questionnaire_result,
        text_result
    )

    recommendation_category = get_recommendation_category(
        final_assessment,
        text_result["prediction"]
    )

    recommendation = get_random_recommendation(
        recommendation_category
    )

    return {
        "questionnaire": questionnaire_result,
        "text": text_result,
        "final_assessment": final_assessment,
        "recommendation": recommendation
    }