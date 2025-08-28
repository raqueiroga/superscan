# SuperScan

Ferramenta simples para verificação de portas em hosts remotos.

## Uso

```bash
python scanner_basic.py [host] -p [portas]
```

Exemplos:

```bash
# Verifica a porta 80 no host especificado
python scanner_basic.py example.com -p 80

# Verifica múltiplas portas
python scanner_basic.py example.com -p 22 80 443
```

O script indicará se cada porta informada está aberta ou fechada.

## Interface web

Uma interface básica via Streamlit está disponível em `tools/ui_app.py`. Execute-a com:

```bash
streamlit run tools/ui_app.py
```

Executar `python tools/ui_app.py` diretamente **não** iniciará a interface.

A interface permite informar um host e uma lista de portas (separadas por vírgula) para verificar quais estão abertas.

## Script de inicialização

Para iniciar rapidamente a interface web sem digitar o comando completo, execute:

```bash
./start.sh
```
O script é um atalho para `streamlit run tools/ui_app.py` e aceita os mesmos argumentos. Se o repositório estiver em `~/superscan`, você pode chamá-lo como `~/superscan/start.sh`.
