
import unittest
from HTMLTestRunner import HTMLTestRunner

discover = unittest.defaultTestLoader.discover(
    start_dir="test_case/order", pattern="test*.py",top_level_dir=None
)

# runner = unittest.TextTestRunner()

file = open("report_20190524.html","wb+")
runner = HTMLTestRunner(
    stream=file,
    title="自动化测试报告",
    description="报告详情"
)
runner.run(discover)