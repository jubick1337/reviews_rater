import torch as torch
from keras.preprocessing.sequence import pad_sequences
from transformers import BertForSequenceClassification, BertTokenizer


class ReviewsModel(torch.nn.Module):
    def __init__(self, device: torch.device):
        super(ReviewsModel, self).__init__()
        self._model = BertForSequenceClassification.from_pretrained(
            "bert-base-uncased",
            num_labels=2,
            output_attentions=False,
            output_hidden_states=False,
            state_dict=torch.load('./ml/weights.pt') if device == 'cpu' else torch.load('./ml/weights.pt',
                                                                                        map_location='cpu')
        ).to(device)
        self._device = device
        self._tokenizer = BertTokenizer.from_pretrained('bert-base-uncased', do_lower_case=True)
        self.max_len = 128

    def forward(self, text: str):
        input_id = self._tokenizer.encode(text, add_special_tokens=True, max_length=self.max_len)
        input_ids = pad_sequences([input_id], maxlen=self.max_len, dtype="long",
                                  value=0, truncating="post", padding="post")
        att_mask = [[int(token_id > 0) for token_id in input_ids[0]]]
        input_id = torch.tensor(input_ids).to(self._device)
        att_mask = torch.tensor(att_mask).to(self._device)
        output = self._model(input_id, att_mask)
        return torch.argmax(torch.nn.functional.softmax(output[0], 1))
