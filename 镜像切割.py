# 用户输入文件路径
input_file = input("请输入要处理的文件路径：").strip()
output_file = input("请输入保存处理后文件的路径：").strip()

# 输入起始和结束地址
start_address = int(input("请输入起始地址 (例如 0x000a0000)：").strip(), 16)
end_address_input = input("请输入结束地址（按 Enter 直接保留到文件结束）：").strip()

# 将结束地址设置为默认值
end_address = int(end_address_input, 16) if end_address_input else None

try:
    with open(input_file, "rb") as infile:
        infile.seek(start_address)  # 跳到起始地址
        if end_address:
            length = end_address - start_address
            data = infile.read(length)  # 读取指定范围的数据
        else:
            data = infile.read()  # 读取起始地址到文件末尾的数据

    with open(output_file, "wb") as outfile:
        outfile.write(data)  # 将读取的数据写入新文件

    print(f"处理完成！保留 {input_file} 的 0x{start_address:08x} 到 "
          f"{'文件末尾' if not end_address else f'0x{end_address:08x}'}，结果保存为 {output_file}")
except FileNotFoundError:
    print(f"错误：文件 {input_file} 未找到，请检查文件路径！")
except ValueError:
    print("错误：起始地址或结束地址格式不正确，请输入十六进制地址（例如 0x000a0000）！")
except Exception as e:
    print(f"发生错误：{e}")

