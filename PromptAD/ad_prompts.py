

class_mapping = {
    "macaroni1": "macaroni",
    "macaroni2": "macaroni",
    "pcb1": "printed circuit board",
    "pcb2": "printed circuit board",
    "pcb3": "printed circuit board",
    "pcb4": "printed circuit board",
    "pipe_fryum": "pipe fryum",
    "chewinggum": "chewing gum",
    "metal_nut": "metal nut"
}



abnormal_state0 = ['damaged {}', 'broken {}', '{} with flaw', '{} with defect', '{} with damage']

#
class_state_abnormal = {
    'bottle': ['{} with large breakage', '{} with small breakage', '{} with contamination'],
    'toothbrush': ['{} with defect', '{} with anomaly'],
    'carpet': ['{} with hole', '{} with color stain', '{} with metal contamination', '{} with thread residue', '{} with thread', '{} with cut'],
    'hazelnut': ['{} with crack', '{} with cut', '{} with hole', '{} with print'],
    'leather': ['{} with color stain', '{} with cut', '{} with fold', '{} with glue', '{} with poke'],
    'cable': ['{} with bent wire', '{} with missing part', '{} with missing wire', '{} with cut', '{} with poke'],
    'capsule': ['{} with crack', '{} with faulty imprint', '{} with poke', '{} with scratch', '{} squeezed with compression'],
    'grid': ['{} with breakage',  '{} with thread residue', '{} with thread', '{} with metal contamination', '{} with glue', '{} with a bent shape'],
    'pill': ['{} with color stain', '{} with contamination', '{} with crack', '{} with faulty imprint', '{} with scratch', '{} with abnormal type'],
    'transistor': ['{} with bent lead', '{} with cut lead', '{} with damage', '{} with misplaced transistor'],
    'metal_nut': ['{} with a bent shape ', '{} with color stain', '{} with a flipped orientation', '{} with scratch'],
    'screw': ['{} with manipulated front',  '{} with scratch neck', '{} with scratch head'],
    'zipper': ['{} with broken teeth', '{} with fabric border', '{} with defect fabric', '{} with broken fabric', '{} with split teeth', '{} with squeezed teeth'],
    'tile': ['{} with crack', '{} with glue strip', '{} with gray stroke', '{} with oil', '{} with rough surface'],
    'wood': ['{} with color stain', '{} with hole', '{} with scratch', '{} with liquid'],

    'candle': ['{} with melded wax', '{} with foreign particals', '{} with extra wax', '{} with chunk of wax missing', '{} with weird candle wick', '{} with damaged corner of packaging', '{} with different colour spot'],
    'capsules': ['{} with scratch', '{} with discolor', '{} with misshape', '{} with leak', '{} with bubble'],
    # 'capsules': [],
    'cashew': ['{} with breakage', '{} with small scratches', '{} with burnt', '{} with stuck together', '{} with spot'],
    'chewinggum': ['{} with corner missing', '{} with scratches', '{} with chunk of gum missing', '{} with colour spot', '{} with cracks'],
    'fryum': ['{} with breakage', '{} with scratches', '{} with burnt', '{} with colour spot', '{} with fryum stuck together', '{} with colour spot'],
    'macaroni1': ['{} with color spot', '{} with small chip around edge', '{} with small scratches', '{} with breakage', '{} with cracks'],
    'macaroni2': ['{} with color spot', '{} with small chip around edge', '{} with small scratches', '{} with breakage', '{} with cracks'],
    'pcb1': ['{} with bent', '{} with scratch', '{} with missing', '{} with melt'],
    'pcb2': ['{} with bent', '{} with scratch', '{} with missing', '{} with melt'],
    'pcb3': ['{} with bent', '{} with scratch', '{} with missing', '{} with melt'],
    'pcb4': ['{} with scratch', '{} with extra', '{} with missing', '{} with wrong place', '{} with damage', '{} with burnt', '{} with dirt'],
    'pipe_fryum': ['{} with breakage', '{} with small scratches', '{} with burnt', '{} with stuck together', '{} with colour spot', '{} with cracks']}


state_anomaly = ["damaged {}",
                 "flawed {}",
                 "abnormal {}",
                 "imperfect {}",
                 "blemished {}",
                 "{} with flaw",
                 "{} with defect",
                 "{} with damage"]


state_normal = [
    "a clean {}",
    "a perfect {}",
    "a flawless {}",
    "a normal {}",
    "an intact {}",
]


class_state_normal = {
    'bottle': ['{} in perfect condition', '{} intact', '{} clean and undamaged'],
    'toothbrush': ['{} without any defects', '{} in normal condition'],
    'carpet': ['{} without holes', '{} with uniform color', '{} free of contamination', '{} without residue', '{} without cuts'],
    'hazelnut': ['{} whole and unbroken', '{} without cuts', '{} without holes', '{} with no printing errors'],
    'leather': ['{} with even color', '{} without cuts', '{} smooth and uncreased', '{} clean and free of glue', '{} without pokes'],
    'cable': ['{} with straight wires', '{} with all parts intact', '{} without missing wires', '{} uncut', '{} unpoked'],
    'capsule': ['{} without cracks', '{} with proper imprint', '{} unpoked', '{} smooth and unscratched', '{} in original shape'],
    'grid': ['{} intact and unbroken', '{} free of residue', '{} without contamination', '{} with proper shape', '{} free of glue'],
    'pill': ['{} without stains', '{} clean and uncontaminated', '{} without cracks', '{} with proper imprint', '{} smooth and unscratched'],
    'transistor': ['{} with straight leads', '{} with uncut leads', '{} undamaged', '{} properly placed'],
    'metal_nut': ['{} with proper shape', '{} clean and unstained', '{} with correct orientation', '{} smooth and unscratched'],
    'screw': ['{} with undamaged front', '{} with smooth neck', '{} with unscratched head'],
    'zipper': ['{} with intact teeth', '{} with proper fabric', '{} without defects', '{} without splits', '{} with smooth teeth'],
    'tile': ['{} without cracks', '{} smooth and clean', '{} free of glue strips', '{} with even surface'],
    'wood': ['{} clean and unstained', '{} without holes', '{} smooth and unscratched', '{} free of liquid residue'],
    'candle': ['{} smooth and even', '{} without foreign particles', '{} with proper wax distribution', '{} with intact wick', '{} with perfect packaging', '{} with uniform color','{} with consistent fragrance distribution','{} with no visible scratches or dents','{} properly labeled with clear instructions','{} with a stable base for safe use'],
    'capsules': ['{} smooth and intact', '{} with uniform color', '{} properly shaped', '{} without leaks', '{} bubble-free'],
    'cashew': ['{} whole and unbroken', '{} smooth and clean', '{} without burns', '{} unstuck', '{} spotless'],
    'chewinggum': ['{} intact and smooth', '{} without scratches', '{} in perfect shape', '{} with uniform color'],
    'fryum': ['{} unbroken and smooth', '{} evenly colored', '{} without burns', '{} separated and clean'],
    'macaroni1': ['{} clean and smooth', '{} without chips', '{} without scratches', '{} unbroken', '{} without cracks'],
    'macaroni2': ['{} clean and smooth', '{} without chips', '{} without scratches', '{} unbroken', '{} without cracks'],
    'pcb1': ['{} straight and undamaged', '{} smooth and unscratched', '{} with all components present', '{} without melting'],
    'pcb2': ['{} straight and undamaged', '{} smooth and unscratched', '{} with all components present', '{} without melting'],
    'pcb3': ['{} straight and undamaged', '{} smooth and unscratched', '{} with all components present', '{} without melting'],
    'pcb4': ['{} smooth and clean', '{} with correct components', '{} without missing parts', '{} properly placed', '{} undamaged and unburnt', '{} free of dirt'],
    'pipe_fryum': ['{} unbroken and smooth', '{} without scratches', '{} evenly colored', '{} separated and clean', '{} without cracks']
}
