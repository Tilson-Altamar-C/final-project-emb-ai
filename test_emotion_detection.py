import unittest
from EmotionDetection.emotion_detection import emotion_detector

TRANSLATE = {
    "anger": "ira",
    "disgust": "desagrado",
    "fear": "miedo",
    "joy": "alegría",
    "sadness": "tristeza",
    None: None,
}

def translate_dominant(dom):
    if dom is None:
        return None
    dom = str(dom).strip().lower()
    return TRANSLATE.get(dom, dom)  # si ya viene en ES, lo deja igual

class TestEmotionDetector(unittest.TestCase):
    def test_joy(self):
        result = emotion_detector("Me alegra que esto haya sucedido")
        self.assertEqual(translate_dominant(result.get("dominant_emotion")), "alegría")

    def test_anger(self):
        result = emotion_detector("Estoy realmente enojado por esto")
        self.assertEqual(translate_dominant(result.get("dominant_emotion")), "ira")

    def test_disgust(self):
        result = emotion_detector("Me siento disgustado solo de oír sobre esto")
        self.assertEqual(translate_dominant(result.get("dominant_emotion")), "desagrado")

    def test_sadness(self):
        result = emotion_detector("Estoy tan triste por esto")
        self.assertEqual(translate_dominant(result.get("dominant_emotion")), "tristeza")

    def test_fear(self):
        result = emotion_detector("Tengo mucho miedo de que esto suceda")
        self.assertEqual(translate_dominant(result.get("dominant_emotion")), "miedo")


if __name__ == "__main__":
    unittest.main()