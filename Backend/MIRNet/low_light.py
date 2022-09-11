def enhance(img):
    from MIRNet.MIRNet.inference import Inferer
    from MIRNet.MIRNet.utils import plot_result
    import time

    start = time.time()
    inferer = Inferer()

    inferer.build_model(num_rrg=3, num_mrb=2, channels=64, weights_path='low_light_weights_best.h5')
    _, output_image = inferer.infer(img)
    print(f' Total time taken: {time.time() - start}')
    return output_image