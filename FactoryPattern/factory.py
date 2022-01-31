class Model():
    def __int__(self):
        pass

class BertModel(Model):
    def __init__(self):
        self.name = "bert"

class Gpt2Model(Model):
    def __init__(self):
        self.name = "gpt2"
    
class ModelFactory:
    def get_model(self,model_name):
        if model_name == "bert":
            return BertModel()
        if model_name == "gpt2":
            return Gpt2Model()

        print(f"还未提供{model_name}模型")

if __name__ == "__main__":
    modelfactory = ModelFactory()
    #如果不用工厂方法，那么需要知道bert 和 gpt2 分别对应的类名
    #而使用了工厂方法，封装工厂类是库提供者的任务，用户只需要提供需要的模型名字即可
    model = modelfactory.get_model("bert")
    print(model.name)
    model = modelfactory.get_model("gpt2")
    print(model.name)
    model = modelfactory.get_model("T5")
