# ☀️🌙 Sky Info API

**Sky Info** é uma API RESTful desenvolvida com **FastAPI** que fornece informações astronômicas sobre o Sol e a Lua com base em uma **data** e uma **cidade**. Ideal para fins educacionais, astronômicos ou para aplicações que dependem de eventos celestes.

---

## 🚀 Funcionalidades

- 📍 Entrada por **nome da cidade** e **data**.
- 🌙 `/moon`: retorna fase da Lua, horários de nascer e pôr da Lua.
- ☀️ `/sun`: retorna horários do nascer e pôr do Sol.
- 🌐 Respostas em formato padronizado UTC.

---

## 🔧 Tecnologias

- **Python 3.11+**
- **FastAPI**
- **Uvicorn**
- **Astral** (para cálculos solares/lunares)
- **Geopy** ou similar (para geocodificação de cidades)

---

## 📦 Instalação

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/sky-info.git
cd sky-info

# (Opcional) Crie e ative um ambiente virtual
python -m venv venv
source venv/bin/activate  # Windows: .\venv\Scripts\activate

# Instale as dependências
pip install -r requirements.txt
