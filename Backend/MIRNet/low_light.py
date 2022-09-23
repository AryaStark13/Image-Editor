from MIRNet.MIRNet.inference import Inferer
inferer = Inferer()

def enhance(img):
    # from MIRNet.MIRNet.inference import Inferer
    import time

    # inferer = Inferer()
    start = time.time()

    # inferer.build_model(num_rrg=3, num_mrb=2, channels=64, weights_path='low_light_weights_best.h5')
    try:
        _, output_image = inferer.infer(img)
    except Exception as e:
        print(e)
        return img, 0
    else:
        total_time = time.time() - start
        print(f' Total time taken: {total_time:.2f} seconds')
        return output_image, total_time
        

def load_model():
    # from MIRNet.MIRNet.inference import Inferer
    # inferer = Inferer()

    try:
        inferer.build_model(num_rrg=3, num_mrb=2, channels=64, weights_path='low_light_weights_best.h5')
    except Exception as e:
        print(e)
        return False, None
    else:
        print('Model loaded successfully')
        # print(inferer.model)
        return True