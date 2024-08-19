h_i, m_i, h_f , m_f = map(int, input().split())

if h_i < h_f:
    h = h_f - h_i
    if m_i < m_f:
        m = m_f - m_i
    if m_i > m_f:
        h = h - 1
        m = (60 - m_i) + m_f
    if m_i == m_f:
        m = 0
        
if h_i > h_f:
    h = (24 - h_i) + h_f
    if m_i < m_f:
        m = m_f - m_i
    if m_i > m_f:
        h = h - 1
        m = (60 - m_i) + m_f
    if m_i == m_f:
        m = 0
        
if h_i == h_f:
    if m_i < m_f:
        m = m_f - m_i
        h = 0
        
    if m_i > m_f:
        m = (60 - m_i) + m_f
        h = 23
        
    if m_i == m_f:
        h = 24
        m = 0
        
print(f'O JOGO DUROU {h} HORA(S) E {m} MINUTO(S)')