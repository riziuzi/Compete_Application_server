from transformers import AutoTokenizer, RobertaForQuestionAnswering
import torch


questions = {
    "time": "what was the time of doing the task?",
    "task": "what was completed task?"
}
# tokenizer = AutoTokenizer.from_pretrained("deepset/roberta-base-squad2")                          #because it is getting imported in server.py
# model = RobertaForQuestionAnswering.from_pretrained("deepset/roberta-base-squad2")

def QnA(text = "Today, I spent 2 hours working on the project. I started by reviewing the project requirements and then moved on to creating a rough outline of the project. I also spent some time researching the best tools to use for the project. I ran into a few issues with the tools, but I was able to resolve them after some troubleshooting. Overall, I feel like I made good progress today and I’m looking forward to continuing to work on the project tomorrow."):
    
    answer = {}
    # text = "In the past three weeks, my focus has been on enhancing both my physical fitness and writing consistency. I kicked off the journey with a modest 30-minute jog, gradually incorporating bodyweight exercises and exploring different workout environments. Simultaneously, I established a daily writing routine, dedicating at least 30 minutes each morning to personal reflections and even delving into short fiction. As I progressed, I extended jogging sessions, introduced a stretching routine, and experimented with diverse workout approaches. Writing has become a grounding practice, helping me clear my mind and set a positive tone for the day. Overall, the combination of physical activity and creative expression has created a symbiotic rhythm, fostering a sense of well-being and accomplishment."
    # text = "Today, I read geography and history from 2 am to 4 am."
    # text="GOING ALONG SLUSHY COUNTRY ROADS AND SPEAKING TO DAMP AUDIENCES IN DRAUGHTY SCHOOL ROOMS DAY AFTER DAY FOR A FORTNIGHT HE'LL HAVE TO PUT IN AN APPEARANCE AT SOME PLACE OF WORSHIP ON SUNDAY MORNING AND HE CAN COME TO US IMMEDIATELY AFTERWARDS".lower()
    # text = "Hello, I think that I completed two notebooks and also read the geography at 2.30 am"
    for question in questions.keys():
        inputs = tokenizer(questions[question], text, return_tensors="pt")
        with torch.no_grad():
            outputs = model(**inputs)

        answer_start_index = outputs.start_logits.argmax()
        answer_end_index = outputs.end_logits.argmax()
        predict_answer_tokens = inputs.input_ids[0, answer_start_index : answer_end_index + 1]
        answer[question] = tokenizer.decode(predict_answer_tokens, skip_special_tokens=True)
    
    return answer




if(__name__=="__main__"):
    print(QnA())