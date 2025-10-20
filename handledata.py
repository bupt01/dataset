# import json
# import os
#
# root_dir = r'E:\PycharmProjects\pythonProject2\InferredBugs-main\inferredbugs\java'
# i=0
# # 遍历所有项目文件夹
# for project_name in os.listdir(root_dir):
#     project_path = os.path.join(root_dir, project_name)
#     if not os.path.isdir(project_path):
#         continue
#
#     seen_bug_content = {}  # 用于存储 (before + after) 内容 -> bug_folder
#
#     # 遍历项目中的所有 bug 子文件夹
#     for bug_folder in os.listdir(project_path):
#         bug_path = os.path.join(project_path, bug_folder)
#         if not os.path.isdir(bug_path):
#             continue
#
#         file_before_path = os.path.join(bug_path, 'file_before.txt')
#         file_after_path = os.path.join(bug_path, 'file_after.txt')
#         commit_info_path=os.path.join(bug_path,'commit_info.json')
#
#         if not os.path.isfile(file_before_path) or not os.path.isfile(file_after_path):
#             continue
#
#         try:
#             with open(file_before_path, 'r', encoding='utf-8') as f1:
#                 before_content = f1.read().strip()
#             with open(file_after_path, 'r', encoding='utf-8') as f2:
#                 after_content = f2.read().strip()
#             with open(commit_info_path, 'r', encoding='utf-8') as f1:
#                 commit_info = json.load(f1)
#                 commit_info = json.dumps(commit_info, sort_keys=True)
#
#         except Exception as e:
#             print(f"[读取失败] {bug_path}，错误：{e}")
#             continue
#
#         combined_content = before_content + '\n====AFTER====\n' + after_content+'\n====COMMIT====\n'+commit_info
#
#         if combined_content in seen_bug_content:
#             existing_folder = seen_bug_content[combined_content]
#             i=i+1
#             print(f"[重复] 项目 {project_name} 中，'{bug_folder}' 与 '{existing_folder}' 的 file_before.txt 和 file_after.txt 内容相同")
#         else:
#             seen_bug_content[combined_content] = bug_folder
# print(i)
#
# import os
# import json
# import shutil
#
# root_dir = r'E:\PycharmProjects\pythonProject2\InferredBugs-main\inferredbugs-after\java'
# i = 0
# j=0
# # 遍历所有项目文件夹
# for project_name in os.listdir(root_dir):
#     project_path = os.path.join(root_dir, project_name)
#     if not os.path.isdir(project_path):
#         continue
#
#     seen_bug_content = {}  # 内容 -> bug_folder
#
#     for bug_folder in os.listdir(project_path):
#         i=i+1
#         bug_path = os.path.join(project_path, bug_folder)
#         if not os.path.isdir(bug_path):
#             continue
#
#         file_before_path = os.path.join(bug_path, 'file_before.txt')
#         file_after_path = os.path.join(bug_path, 'file_after.txt')
#         commit_info_path = os.path.join(bug_path, 'commit_info.json')
#         bug_json_path = os.path.join(bug_path, 'bug.json')
#
#         if not os.path.isfile(file_before_path) or not os.path.isfile(file_after_path):
#             continue
#
#         try:
#             with open(file_before_path, 'r', encoding='utf-8') as f1:
#                 before_content = f1.read().strip()
#             with open(file_after_path, 'r', encoding='utf-8') as f2:
#                 after_content = f2.read().strip()
#             with open(commit_info_path, 'r', encoding='utf-8') as f3:
#                 commit_info = json.load(f3)
#                 commit_info = json.dumps(commit_info, sort_keys=True)
#
#
#         except Exception as e:
#             print(f"[读取失败] {bug_path}，错误：{e}")
#             continue
#
#         combined_content = before_content + '\n====AFTER====\n' + after_content + '\n====COMMIT====\n' + commit_info
#
#         if combined_content in seen_bug_content:
#             existing_folder = seen_bug_content[combined_content]
#             j += 1
#             print(f"[重复] 项目 {project_name} 中，'{bug_folder}' 与 '{existing_folder}' 的内容重复")
#
#             # 读取当前重复的 bug_folder 下的 bug.json 内容
#             source_bug_json = os.path.join(bug_path, 'bug.json')
#             target_bug_json = os.path.join(os.path.join(project_path, existing_folder), 'bug.json')
#
#             if os.path.exists(source_bug_json):
#                 try:
#                     with open(source_bug_json, 'r', encoding='utf-8') as src_f:
#                         new_bugs = json.load(src_f)
#
#                     # 如果目标 bug.json 存在，读取并合并，否则创建新列表
#                     if os.path.exists(target_bug_json):
#                         with open(target_bug_json, 'r', encoding='utf-8') as tgt_f:
#                             old_bugs = json.load(tgt_f)
#                     else:
#                         old_bugs = []
#
#                     # 合并并写回目标文件
#                     # combined_bugs = [new_bugs,old_bugs]
#                     # with open(target_bug_json, 'w', encoding='utf-8') as tgt_f:
#                     #     json.dump(combined_bugs, tgt_f, indent=2)
#
#                     print(f"✅ 已将 {bug_folder} 的 bug.json 合并到 {existing_folder} 中")
#
#                 except Exception as e:
#                     print(f"[合并失败] 读取或写入 bug.json 出错：{e}")
#
#             # 删除重复的 bug 文件夹
#             try:
#                 # shutil.rmtree(bug_path)
#                 print(f"🗑️ 删除了重复的文件夹：{bug_folder}")
#             except Exception as e:
#                 print(f"[删除失败] 无法删除 {bug_folder}：{e}")
#
#         else:
#             seen_bug_content[combined_content] = bug_folder
#
# print(f"\n共发现重复并合并 {i} 个 bug 文件夹。")
# print(f"\n共发现重复并合并 {j} 个 bug 文件夹。")

# import os
# import json
#
# root_dir = r'E:\PycharmProjects\pythonProject2\InferredBugs-main\inferredbugs-after\java'
# i = 0  # 项目数
# j = 0  # 被转换的 bug.json 文件数
#
# def flatten_to_dict_list(obj):
#     """将任意嵌套结构展平为 [dict, dict, ...]"""
#     result = []
#     if isinstance(obj, dict):
#         result.append(obj)
#     elif isinstance(obj, list):
#         for item in obj:
#             result.extend(flatten_to_dict_list(item))  # 递归 flatten
#     return result
#
# for project_name in os.listdir(root_dir):
#     project_path = os.path.join(root_dir, project_name)
#     if not os.path.isdir(project_path):
#         continue
#
#     for bug_folder in os.listdir(project_path):
#         bug_path = os.path.join(project_path, bug_folder)
#         bug_json_path = os.path.join(bug_path, 'bug.json')
#
#         if not os.path.exists(bug_json_path):
#             continue
#
#         try:
#             with open(bug_json_path, 'r', encoding='utf-8') as f:
#                 data = json.load(f)
#
#             flat_data = flatten_to_dict_list(data)
#
#             # 只有在格式有变化时才写回
#             if not (isinstance(data, list) and all(isinstance(d, dict) for d in data)):
#                 with open(bug_json_path, 'w', encoding='utf-8') as f:
#                     json.dump(flat_data, f, indent=2)
#                 j += 1
#
#         except Exception as e:
#             print(f"Error processing {bug_json_path}: {e}")
#
#     i += 1
#
# print(f"共处理 {i} 个项目，标准化了 {j} 个 bug.json 文件的格式。")


# import os
# import json
# import shutil
#
# root_dir = r'E:\PycharmProjects\pythonProject2\InferredBugs-main\inferredbugs-after\java'
# i=0
# j=0
# for project_name in os.listdir(root_dir):
#     project_path = os.path.join(root_dir, project_name)
#     if not os.path.isdir(project_path):
#         continue
#
#     for bug_folder in os.listdir(project_path):
#         j=j+1
#         bug_path = os.path.join(project_path, bug_folder)
#         bug_json_path = os.path.join(bug_path, 'bug.json')
#
#         if not os.path.isfile(bug_json_path):
#             continue
#
#         try:
#             with open(bug_json_path, 'r', encoding='utf-8') as f:
#                 bug_list = json.load(f)
#         except Exception as e:
#             print(f"读取 JSON 出错：{bug_json_path}，错误信息：{e}")
#             continue
#
#         all_invalid = True  # 假设所有都是非法的，直到找到一个合法的
#
#         for bug in bug_list:
#             if not isinstance(bug, dict):
#                 continue
#             bug_trace = bug.get("bug_trace", [])
#             if not isinstance(bug_trace, list) or len(bug_trace) == 0:
#                 continue
#
#             # 提取所有非 None 的 filename
#             filenames = [item.get("filename") for item in bug_trace if isinstance(item, dict) and "filename" in item]
#             if len(filenames) == 0:
#                 continue
#
#             # 判断所有 filename 是否一致
#             if all(fname == filenames[0] for fname in filenames):
#                 all_invalid = False
#                 break  # 有一个合法就跳出
#             else:
#                 i=i+1
#                 print(f"有些 bug 不合法：{bug_path}")
#
#         if all_invalid:
#             i=i+1
#             print(f"所有 bug 都不合法：{bug_path}")
#             try:
#                 shutil.rmtree(bug_path)
#                 # print(f"🗑️ 删除了重复的文件夹：{bug_folder}")
#             except Exception as e:
#                 print(f"[删除失败] 无法删除 {bug_folder}：{e}")
#
# print(i)

import os
import json

root_dir = r'E:\PycharmProjects\pythonProject2\InferredBugs-main\inferredbugs-filtered\java'
i=0
for project_name in os.listdir(root_dir):
    project_path = os.path.join(root_dir, project_name)
    if not os.path.isdir(project_path):
        continue

    for bug_folder in os.listdir(project_path):
        i=i+1
        bug_path = os.path.join(project_path, bug_folder)
        bug_json_path = os.path.join(bug_path, 'bug.json')

        if not os.path.isfile(bug_json_path):
            continue

        try:
            with open(bug_json_path, 'r', encoding='utf-8') as f:
                bug_list = json.load(f)
        except Exception as e:
            print(f"读取 JSON 出错：{bug_json_path}，错误信息：{e}")
            continue

        new_bug_list = []

        for bug in bug_list:
            if not isinstance(bug, dict):
                continue
            bug_trace = bug.get("bug_trace", [])
            if not isinstance(bug_trace, list) or len(bug_trace) == 0:
                continue

            filenames = [item.get("filename") for item in bug_trace if isinstance(item, dict) and "filename" in item]
            if len(filenames) == 0:
                continue

            if all(fname == filenames[0] for fname in filenames):
                new_bug_list.append(bug)  # 只有合法的才保留

        # 如果有修改，覆盖写回文件
        if len(new_bug_list) < len(bug_list):
            pass
            # try:
            #     with open(bug_json_path, 'w', encoding='utf-8') as f:
            #         json.dump(new_bug_list, f, indent=2, ensure_ascii=False)
            #     print(f"已删除非法 bug，更新文件：{bug_json_path}")
            # except Exception as e:
            #     print(f"写入 JSON 出错：{bug_json_path}，错误信息：{e}")
print(i)