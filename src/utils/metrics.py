import numpy as np

# def iou_metric(y_true, y_pred, threshold=0.5):
#     y_pred = y_pred > threshold
#     intersection = np.logical_and(y_true, y_pred)
#     union = np.logical_or(y_true, y_pred)
#     iou = np.sum(intersection) / np.sum(union)
#     return iou
def iou_metric(y_true, y_pred):
    if y_pred.shape[-1] == 1:
        y_pred = np.squeeze(y_pred, axis=-1)

    intersection = np.logical_and(y_true, y_pred)
    union = np.logical_or(y_true, y_pred)
    iou = np.sum(intersection) / np.sum(union)
    return iou


if __name__ == "__main__":
    y_true = np.random.randint(0, 2, (10, 256, 256, 1))
    y_pred = np.random.rand(10, 256, 256, 1)
    print(f"IOU: {iou_metric(y_true, y_pred):.4f}")


