![Normalization](https://pics.spark-in.me/upload/7c12fea58ff515ffb46df52b6050ace0.jpg)

# Russian STT Text Normalization

Russian text normalization pipeline for speech-to-text and other applications based on tagging s2s networks.

**Форк с улучшениями:**
- ✅ Поддержка PyTorch 2.x
- ✅ Современный `pyproject.toml` для установки через pip/uv
- ✅ Автоматический поиск файла модели
- ✅ Понятные сообщения об ошибках
- 📦 Упаковка модели в пакет

## Установка

### Через pip/uv (рекомендуется)

```bash
pip install git+https://github.com/bzikst/russian_stt_text_normalization.git
```

Или с помощью uv:

```bash
uv pip install git+https://github.com/bzikst/russian_stt_text_normalization.git
```

### Через pyproject.toml

Добавьте в ваш `pyproject.toml`:

```toml
dependencies = [
    "russian-stt-text-normalization",
]

[tool.uv.sources]
russian-stt-text-normalization = { git = "https://github.com/bzikst/russian_stt_text_normalization.git" }
```

## Requirements

- Python >= 3.8
- [PyTorch](https://pytorch.org/get-started/locally/) >= 1.4 (рекомендуется >= 2.0)
- [tqdm](https://github.com/tqdm/tqdm) для прогресс-бара

## Usage

```python
from normalizer import Normalizer

text = 'С 12.01.1943 г. площадь сельсовета — 1785,5 га.'

norm = Normalizer()
result = norm.norm_text(text)
print(result)
```

```
>>> С двенадцатого января тысяча девятьсот сорок третьего года площадь сельсовета
>>> — тысяча семьсот восемьдесят пять целых и пять десятых гектара
```

## PyTorch 2.x Compatibility

⚠️ **Важно**: Модель `jit_s2s.pt` использует устаревший формат PyTorch 1.x и несовместима с PyTorch 2.x.

### Решение

Вам нужно конвертировать модель в новый формат. См. подробные инструкции в [UPGRADE.md](UPGRADE.md).

**Кратко:**
1. Используйте машину с Python 3.8-3.10 и PyTorch 1.13
2. Запустите `python convert_model.py`
3. Получите файл `jit_s2s_v2.pt`, совместимый с PyTorch 2.x

После конвертации модуль автоматически будет использовать новый формат.

## Оригинальный репозиторий

Оригинал: https://github.com/snakers4/russian_stt_text_normalization

**Автор**: snakers4  
**Форк поддерживается**: bzikst
