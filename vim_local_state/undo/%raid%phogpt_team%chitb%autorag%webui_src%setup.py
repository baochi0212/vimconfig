Vim�UnDo� �1~/[?�w��rXI�c����{�Ľmm   M       N                           gY=�    _�                             ����                                                                                                                                                                                                                                                                                                                                                             gY=�     �          N      	import os�         N    5��                        1                   1       5�_�                       9    ����                                                                                                                                                                                                                                                                                                                                                             gY=�     �          N      :./FlagEmbedding/research/BGE_M3/test_distill_381/import os5��        9                 9                     5�_�                    1       ����                                                                                                                                                                                                                                                                                                                            1          2           v        gY=�     �   0   2   N      I        long_description=open("README.md", "r", encoding="utf-8").read(),   6        long_description_content_type="text/markdown",5��    0                    �      C               5�_�                    1       ����                                                                                                                                                                                                                                                                                                                            1          1          v        gY=�     �   0   2   M      =               long_description_content_type="text/markdown",5��    0                     �                     5�_�                    1       ����                                                                                                                                                                                                                                                                                                                            1          1          v        gY=�    �   N               �               M   :./FlagEmbedding/research/BGE_M3/test_distill_381/import o0   	import re       +from setuptools import find_packages, setup           # def get_version():   [#     with open(os.path.join("src", "llamafactory", "cli.py"), "r", encoding="utf-8") as f:   !#         file_content = f.read()   >#         pattern = r"{}\W*=\W*\"([^\"]+)\"".format("VERSION")   8#         (version,) = re.findall(pattern, file_content)   #         return version           def get_requires():   >    with open("requirements.txt", "r", encoding="utf-8") as f:           file_content = f.read()   g        lines = [line.strip() for line in file_content.strip().split("\n") if not line.startswith("#")]           return lines           extra_require = {   !    # "torch": ["torch>=1.13.1"],   K    # "torch_npu": ["torch==2.1.0", "torch-npu==2.1.0.post3", "decorator"],   2    "metrics": ["nltk", "jieba", "rouge-chinese"],   2    # "deepspeed": ["deepspeed>=0.10.0,<=0.14.0"],   -    "bitsandbytes": ["bitsandbytes>=0.39.0"],   -    "transformers": ["transformers>=4.41.2"],       "vllm": ["vllm>=0.4.3"],       "galore": ["galore-torch"],       "badam": ["badam"],   4    "gptq": ["optimum>=1.16.0", "auto-gptq>=0.5.0"],       "awq": ["autoawq"],   !    "aqlm": ["aqlm[gpu]>=1.1.0"],   :    "qwen": ["tiktoken", "transformers_stream_generator"],   !    "modelscope": ["modelscope"],       "quality": ["ruff"],       }           def main():   
    setup(           name="webui_interface",           version="0.1",           author="hiyouga",   1        author_email="hiyouga" "@" "buaa.edu.cn",   <        description="Easy-to-use LLM fine-tuning framework",   6        long_description_content_type="text/markdown",   k        keywords=["LLaMA", "BLOOM", "Falcon", "LLM", "ChatGPT", "transformer", "pytorch", "deep learning"],   %        license="Apache 2.0 License",   7        url="https://github.com/hiyouga/LLaMA-Factory",            package_dir={"": "src"},   &        packages=find_packages("src"),   "        python_requires=">=3.8.0",   (        install_requires=get_requires(),   '        # extras_require=extra_require,   Y        # entry_points={"console_scripts": ["llamafactory-cli = llamafactory.cli:main"]},           classifiers=[   -            "Development Status :: 4 - Beta",   .            "Intended Audience :: Developers",   -            "Intended Audience :: Education",   4            "Intended Audience :: Science/Research",   A            "License :: OSI Approved :: Apache Software License",   1            "Operating System :: OS Independent",   2            "Programming Language :: Python :: 3",   4            "Programming Language :: Python :: 3.8",   4            "Programming Language :: Python :: 3.9",   5            "Programming Language :: Python :: 3.10",   5            "Programming Language :: Python :: 3.11",   I            "Topic :: Scientific/Engineering :: Artificial Intelligence",   
        ],       )           if __name__ == "__main__":   
    main()5��            L   
   N               �
      �
      �    N                      �
                     5�_�                            ����                                                                                                                                                                                                                                                                                                                               9                  v        gY=�     �         N      :./FlagEmbedding/research/BGE_M3/test_distill_381/import o05��               :           6       :               5�_�                             ����                                                                                                                                                                                                                                                                                                                               9                  v        gY=�    �   M               �               N   +from setuptools import find_packages, setup   	import re               # def get_version():   [#     with open(os.path.join("src", "llamafactory", "cli.py"), "r", encoding="utf-8") as f:   !#         file_content = f.read()   >#         pattern = r"{}\W*=\W*\"([^\"]+)\"".format("VERSION")   8#         (version,) = re.findall(pattern, file_content)   #         return version           def get_requires():   >    with open("requirements.txt", "r", encoding="utf-8") as f:           file_content = f.read()   E        lines = [line.strip() for line in file_content.strip().split(   .            "\n") if not line.startswith("#")]           return lines           extra_require = {   !    # "torch": ["torch>=1.13.1"],   K    # "torch_npu": ["torch==2.1.0", "torch-npu==2.1.0.post3", "decorator"],   2    "metrics": ["nltk", "jieba", "rouge-chinese"],   2    # "deepspeed": ["deepspeed>=0.10.0,<=0.14.0"],   -    "bitsandbytes": ["bitsandbytes>=0.39.0"],   -    "transformers": ["transformers>=4.41.2"],       "vllm": ["vllm>=0.4.3"],       "galore": ["galore-torch"],       "badam": ["badam"],   4    "gptq": ["optimum>=1.16.0", "auto-gptq>=0.5.0"],       "awq": ["autoawq"],   !    "aqlm": ["aqlm[gpu]>=1.1.0"],   :    "qwen": ["tiktoken", "transformers_stream_generator"],   !    "modelscope": ["modelscope"],       "quality": ["ruff"],       }           def main():   
    setup(           name="webui_interface",           version="0.1",           author="hiyouga",   1        author_email="hiyouga" "@" "buaa.edu.cn",   <        description="Easy-to-use LLM fine-tuning framework",   6        long_description_content_type="text/markdown",   ?        keywords=["LLaMA", "BLOOM", "Falcon", "LLM", "ChatGPT",   =                  "transformer", "pytorch", "deep learning"],   %        license="Apache 2.0 License",   7        url="https://github.com/hiyouga/LLaMA-Factory",            package_dir={"": "src"},   &        packages=find_packages("src"),   "        python_requires=">=3.8.0",   (        install_requires=get_requires(),   '        # extras_require=extra_require,   Y        # entry_points={"console_scripts": ["llamafactory-cli = llamafactory.cli:main"]},           classifiers=[   -            "Development Status :: 4 - Beta",   .            "Intended Audience :: Developers",   -            "Intended Audience :: Education",   4            "Intended Audience :: Science/Research",   A            "License :: OSI Approved :: Apache Software License",   1            "Operating System :: OS Independent",   2            "Programming Language :: Python :: 3",   4            "Programming Language :: Python :: 3.8",   4            "Programming Language :: Python :: 3.9",   5            "Programming Language :: Python :: 3.10",   5            "Programming Language :: Python :: 3.11",   I            "Topic :: Scientific/Engineering :: Artificial Intelligence",   
        ],       )           if __name__ == "__main__":   
    main()5��            M   
   M               �
      �
      �    M                      �
                     5��