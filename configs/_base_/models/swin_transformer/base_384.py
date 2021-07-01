# model settings
# Only for evaluation
model = dict(
    type='ImageClassifier',
    backbone=dict(
        type='SwinTransformer',
        arch='base',
        img_size=384,
        stage_cfg=dict(block_cfg=dict(window_size=12))),
    neck=dict(type='GlobalAveragePooling', dim=1),
    head=dict(
        type='LinearClsHead',
        num_classes=1000,
        in_channels=1024,
        loss=dict(type='CrossEntropyLoss', loss_weight=1.0),
        topk=(1, 5)))
