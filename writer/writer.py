import logging
import csv
import math
import pandas as pd
import numpy as np
from .process_sql import tokenize
import json

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Writer:
    def write():
        pass

class WriterSQL(Writer):
  def write(self, dataset, file_path, db_name):
    sqls = []
    for key, value in dataset.items():
            # sql shared for utterance and all paraphrases
            sql_group = value[0][11]
            if str(sql_group) != 'nan':

                for index, v in enumerate(value):
                    if str(v[7]) != 'nan' and str(v[7]) != ' ':
                        data = self.get_object_info(sql_group, db_name, str(key) + '_' + str(index))
                        sqls.append(data)
    
    with open(file_path,'w') as tsv_file:
      tsv_writer = csv.writer(tsv_file, delimiter='\t')
      for sql in sqls:
          print(sql)
          tsv_writer.writerow([sql['query'], sql['db_id'], sql['id']])
      tsv_file.close()


  def get_object_info(self, sql_str, db_name, id):
        data = {}
        data["query"] = sql_str
        data["db_id"] = db_name
        data["id"] = id
        return data

class WriterSQLFirst(Writer):
  def write(self, dataset, file_path, db_name):
    sqls = []
    for key, value in dataset.items():
            # sql shared for utterance and all paraphrases
            sql_group = value[0][15]
            if str(sql_group) != 'nan':
              if str(value[0][11]) != 'nan' and str(value[0][11]) != ' ':
                data = self.get_object_info(sql_group, db_name, str(key) + '_0')
                sqls.append(data)
    
    with open(file_path,'w') as tsv_file:
      tsv_writer = csv.writer(tsv_file, delimiter='\t')
      for sql in sqls:
          print(sql)
          tsv_writer.writerow([sql['query'], sql['db_id'], sql['id']])
      tsv_file.close()


  def get_object_info(self, sql_str, db_name, id):
        data = {}
        data["query"] = sql_str
        data["db_id"] = db_name
        data["id"] = id
        return data

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

class WriterJsonLikeSpider(Writer):
    def write(self, dataset, file_path, db_name):
        json_data = []
        sql_group = ''
        class_e_c = ''
        class_p = ''
        class_w = ''
        class_geral = ''
        relevance = ''
        ambiguity = ''
        count_questions = 0
        count_total = 0 
        count_no_sql = 0
        count_sql = 0
        for key, value in dataset.items():
            # sql shared for utterance and all paraphrases
            sql_group = value[0][10]
            class_e_c = value[0][14]
            class_p = value[0][15]
            class_w = value[0][16]
            class_geral = value[0][17]
            relevance = value[0][18]
            ambiguity = value[0][21]

            count_total += len(value)
            if str(sql_group) != 'nan':
                for index, v in enumerate(value):
                  count_questions += 1
                  data = self.get_object_info(sql_group, db_name, v[7], str(key) + '_' + str(index), v[8],
                            class_e_c, class_p, class_w, class_geral, relevance, ambiguity)
                  json_data.append(data)
            else:
                count_no_sql +=1

        
        with open(file_path, 'wt', encoding='utf-8') as out:
            json.dump(json_data, out, ensure_ascii=False, sort_keys=True, indent=4, separators=(',', ': '))
            out.close()
        
        print(count_questions)
        print(count_total)
        print(count_no_sql)
        print(count_sql)
    def get_object_info(self, sql_str, db_name, question, id, u_class, class_e_c, class_p, class_w, class_geral, relevance, ambiguity):
        print(question)
        data = {}
        data["id"] = id
        data["db_id"] = db_name
        data["query"] = sql_str
        data["query_toks"] = tokenize(sql_str, True)
        data["question"] = question
        data["question_toks"] = tokenize(question, False)
        data["u_class"] = str(u_class)
        data["class_e_c"] = class_e_c
        data["class_p"] = class_p
        data["class_w"] = class_w
        data["class_geral"] = class_geral
        data["relevance"] = str(relevance)
        data["ambiguity"] = str(ambiguity)
        return data

class WriterJsonLikeSpiderFirst(Writer):
    def write(self, dataset, file_path, db_name):
        json_data = []
        sql_group = ''
        class_e_c = ''
        class_p = ''
        class_w = ''
        class_geral = ''
        relevance = ''
        ambiguity = ''
        count_questions = 0
        count_total = 0
        count_no_sql = 0
        for key, value in dataset.items():
            # sql shared for utterance and all paraphrases
            sql_group = value[0][15]
            class_e_c = value[0][17]
            class_p = value[0][18]
            class_w = value[0][19]
            class_geral = value[0][20]
            relevance = value[0][21]
            ambiguity = value[0][23]

            count_total += len(value)
            if str(sql_group) != 'nan':
              if str(value[0][11]) != 'nan' and str(value[0][11]) != ' ':
                  count_questions += 1
                  data = self.get_object_info(sql_group, db_name, value[0][11], str(key) + '_0' , value[0][12],
                            class_e_c, class_p, class_w, class_geral, relevance, ambiguity)
                  json_data.append(data)
            else:
                count_no_sql +=1

        
        with open(file_path, 'wt', encoding='utf-8') as out:
            json.dump(json_data, out, ensure_ascii=False, sort_keys=True, indent=4, separators=(',', ': '))
            out.close()
        
        print(count_questions)
        print(count_total)
        print(count_no_sql)

    def get_object_info(self, sql_str, db_name, question, id, u_class, class_e_c, class_p, class_w, class_geral, relevance, ambiguity):
        data = {}
        data["id"] = id
        data["db_id"] = db_name
        data["query"] = sql_str
        data["query_toks"] = tokenize(sql_str)
        data["question"] = question
        data["question_toks"] = tokenize(question)
        data["u_class"] = str(u_class)
        data["class_e_c"] = class_e_c
        data["class_p"] = class_p
        data["class_w"] = class_w
        data["class_geral"] = class_geral
        data["relevance"] = str(relevance)
        data["ambiguity"] = str(ambiguity)
        return data