#!/usr/bin/env python3
"""
Скрипт для конвертации старой модели JIT в новый формат PyTorch.

Использование:
    python convert_model.py
"""

import torch
from pathlib import Path

def convert_legacy_model(input_path: str, output_path: str):
    """Конвертирует legacy модель в новый формат."""
    print(f"PyTorch версия: {torch.__version__}")
    print(f"Загрузка модели из: {input_path}")
    
    try:
        # Пытаемся загрузить старую модель
        # В PyTorch 2.x это может не работать напрямую
        model = torch.jit.load(input_path, map_location='cpu')
        print("✓ Модель успешно загружена")
        
        # Сохраняем в новом формате
        print(f"Сохранение модели в: {output_path}")
        torch.jit.save(model, output_path)
        print("✓ Модель успешно сконвертирована")
        
        # Проверяем, что новая модель загружается
        print("Проверка новой модели...")
        test_model = torch.jit.load(output_path, map_location='cpu')
        print("✓ Новая модель успешно загружается")
        
        return True
        
    except Exception as e:
        print(f"✗ Ошибка при конвертации: {e}")
        print("\nВозможные решения:")
        print("1. Используйте PyTorch 1.x для конвертации:")
        print("   python3 -m pip install 'torch<2.0' --force-reinstall")
        print("   python convert_model.py")
        print("   python3 -m pip install 'torch>=2.0' --force-reinstall")
        print("\n2. Или используйте Docker с PyTorch 1.x")
        return False


if __name__ == "__main__":
    input_model = "jit_s2s.pt"
    output_model = "jit_s2s_v2.pt"
    backup_model = "jit_s2s_legacy.pt"
    
    if not Path(input_model).exists():
        print(f"✗ Файл {input_model} не найден")
        exit(1)
    
    # Создаем бэкап
    if not Path(backup_model).exists():
        import shutil
        shutil.copy(input_model, backup_model)
        print(f"✓ Создан бэкап: {backup_model}")
    
    success = convert_legacy_model(input_model, output_model)
    
    if success:
        print("\n" + "="*50)
        print("КОНВЕРТАЦИЯ ЗАВЕРШЕНА УСПЕШНО")
        print("="*50)
        print(f"\nСтарая модель: {input_model} (бэкап: {backup_model})")
        print(f"Новая модель: {output_model}")
        print("\nТеперь обновите normalizer.py для использования jit_s2s_v2.pt")
    else:
        exit(1)

