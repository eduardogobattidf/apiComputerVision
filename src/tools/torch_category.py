import torch
import torch.nn as nn
from torchvision import transforms, models
from PIL import Image
import requests
from io import BytesIO



class ImageClassifier:
    def __init__(self):
        self.model_path = "./src/files/resnet50_model.pth" #arquivo do modelo treinado
        self.class_names = ['berco', 'body', 'cadeira_alimentacao', 'cadeirinha', 'calcado_infantil', 'carrinho_bebe', 'motoca'] #categorias treinadas
        self.device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu") #verifica se tem GPU disponivel
        self.model = self.load_model()
        self.model = self.model.to(self.device)
        self.model.eval()
    #carrega o modelo para uso
    def load_model(self):
        model = models.resnet50(pretrained=False)
        num_ftrs = model.fc.in_features
        model.fc = nn.Linear(num_ftrs, len(self.class_names))
        model.load_state_dict(torch.load(self.model_path, map_location=self.device))
        return model
    #Processa a imagem usando transforms
    def process_image(self, image):
        preprocess = transforms.Compose([
            transforms.Resize(256),
            transforms.CenterCrop(224),
            transforms.ToTensor(),
            transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
        ])
        image = preprocess(image).unsqueeze(0).to(self.device)
        return image
    #Execuao principal para fazer o download da imagem e processar no modelo
    def predict(self, image_url):
        response = requests.get(image_url)
        image = Image.open(BytesIO(response.content)).convert('RGB')
        image = self.process_image(image)
        outputs = self.model(image)
        _, preds = torch.max(outputs, 1)
        return self.class_names[preds[0]]