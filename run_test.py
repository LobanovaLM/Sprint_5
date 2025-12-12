#!/usr/bin/env python3
"""Скрипт для запуска всех тестов"""

import subprocess
import sys
import os


def run_tests():
    """Запуск тестов с помощью pytest"""
    
    # Создаем директорию для отчетов, если ее нет
    os.makedirs("reports", exist_ok=True)
    
    cmd = [
        sys.executable, "-m", "pytest",
        "tests/",
        "-v",  # Подробный вывод
        "--tb=short",  # Короткий traceback
        # "-n", "auto",  # Параллельный запуск (опционально, можно закомментировать)
        "--html=reports/report.html",  # HTML отчет
        "--self-contained-html"
    ]
    
    print(f"Запуск команды: {' '.join(cmd)}")
    
    result = subprocess.run(cmd)
    
    if result.returncode == 0:
        print("\n✓ Все тесты прошли успешно!")
    else:
        print(f"\n✗ Некоторые тесты завершились с ошибкой (код: {result.returncode})")
    
    return result.returncode


if __name__ == "__main__":
    exit_code = run_tests()
    sys.exit(exit_code)