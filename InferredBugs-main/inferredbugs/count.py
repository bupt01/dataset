import os


def count_lines(filepath):
    """统计单个文件的行数"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return sum(1 for _ in f)
    except Exception as e:
        print(f"无法读取文件 {filepath}: {e}")
        return 0


def find_and_count_files(directory):
    """递归查找并统计所有file_before.txt文件的行数"""
    line_counts = []

    for root, _, files in os.walk(directory):
        for file in files:
            if file == "file_before.txt":
                filepath = os.path.join(root, file)
                lines = count_lines(filepath)
                line_counts.append(lines)
                print(f"{filepath}: {lines} 行")

    return line_counts


def calculate_average(line_counts):
    """计算平均值"""
    if not line_counts:
        return 0
    return sum(line_counts) / len(line_counts)


def main():
    current_dir = os.getcwd()
    current_dir=os.path.join(current_dir,"java")
    print(f"正在扫描目录: {current_dir}")

    line_counts = find_and_count_files(current_dir)

    if not line_counts:
        print("未找到任何 file_before.txt 文件")
        return

    total_files = len(line_counts)
    total_lines = sum(line_counts)
    average_lines = calculate_average(line_counts)

    print("\n统计结果:")
    print(f"找到的 file_before.txt 文件总数: {total_files}")
    print(f"总行数: {total_lines}")
    print(f"平均行数: {average_lines:.2f}")


if __name__ == "__main__":
    main()