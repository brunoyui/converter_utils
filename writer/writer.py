import logging
import csv
import math
import pandas as pd
import numpy as np

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Writer:
    def write():
        pass

class WriterCSV(Writer):
    def write(self, dataset, file_path):
        with open(file_path,'w') as tsv_file:
            tsv_writer = csv.writer(tsv_file, delimiter='\t')
            for key, value in dataset.items():
                if math.isnan(float(value[0][4])):
                    value[0][4] = key
                tsv_writer.writerow(value[0])
            tsv_file.close()

class WriterExcel(Writer):
    order_by_similarity = [2667, 3014, 2859, 2824, 2735, 2862, 21, 2775, 2695, 19, 2841, 24, 2850, 13, 2880, 20, 2865, 2894, 2875, 2855, 2899, 25, 2806, 6, 2713, 2756, 2723, 2837, 2717, 2821, 2886, 2722, 2851, 2861, 2688, 2672, 2724, 8, 2860, 7, 2714, 2719, 2791, 3003, 3009, 2835, 2815, 2842, 2868, 2852, 2725, 16, 18, 2690, 15, 2844, 5, 2805, 10, 2721, 2800, 2677, 3007, 3001, 2748, 12, 2759, 14, 4, 1, 2674, 2669, 2, 2709, 3018, 3017, 11, 2738, 2822, 2826, 2870, 2898, 2718, 3, 2771, 3015, 2766, 2892, 2823, 2817, 2799, 2848, 2681, 2783, 2896, 2874, 2884, 2871, 2834, 2792, 2819, 2869, 2845, 2828, 2778, 2678, 2745, 2750, 3005, 23, 2891, 3004, 2761, 17, 2857, 2680, 2816, 2668, 2686, 2758, 2802, 2883, 2743, 2726, 2712, 2833, 2897, 9, 2720, 3013, 2829, 2744, 2675, 2737, 2704, 2818, 2843, 2746, 3016, 2676, 2879, 2789, 2769, 2790, 2734, 2858, 2811, 2773, 2754, 2693, 2781, 22, 2867, 2671, 2694, 2715, 2753, 2887, 2741, 2885, 2830, 2801, 2736, 2780, 2776, 26, 2696, 2683, 2866, 2689, 2679, 2787, 2673, 2795, 2882, 2788, 2804, 27, 2764, 3000, 3012, 2854, 2895, 2670, 2796, 2864, 2849]
    def write(self, dataset, file_path):
        lst = []
        data_frame = pd.DataFrame()
        for k in self.order_by_similarity:
            values = dataset[str(k)]
            for v in values:
                lst.append(v)
            lst.append(pd.Series(np.nan * 17))
        data_frame = pd.DataFrame(lst)
        data_frame.to_excel(file_path)  


class WriterConsole(Writer):
    def write(self, dataset):
        count = 0
        for key, value in dataset.items():
            count += len(value)
            print(str(key), '->', len(value))
        print(count)