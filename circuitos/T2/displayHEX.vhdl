library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity logic_circuit is
    Port ( s : in STD_LOGIC_VECTOR (3 downto 0);  -- Entrada de 4 bits
           a : out STD_LOGIC;
           b : out STD_LOGIC;
           c : out STD_LOGIC;
           d : out STD_LOGIC;
           e : out STD_LOGIC;
           f : out STD_LOGIC;
           g : out STD_LOGIC );
end logic_circuit;

architecture Behavioral of logic_circuit is
begin
    -- Atribuição para a saída a
    a <= (not s(2) and not s(0)) or 
         (not s(3) and s(1)) or 
         (not s(3) and s(2) and s(0)) or 
         (s(3) and not s(2) and not s(1)) or 
         (s(3) and not s(0)) or 
         (s(2) and s(1));

    -- Atribuição para a saída b
    b <= (not s(3) and not s(1) and not s(0)) or 
         (not s(3) and s(1) and s(0)) or 
         (not s(2) and not s(0)) or 
         (s(3) and not s(1) and not s(0)) or 
         (s(3) and not s(2));

    -- Atribuição para a saída c
    c <= (not s(3) and s(2)) or 
         (s(3) and not s(2)) or 
         (not s(1) and s(0)) or 
         (not s(3) and not s(1)) or 
         (not s(3) and s(0));

    -- Atribuição para a saída d
    d <= (s(2) and not s(1) and not s(0)) or 
         (not s(3) and not s(2) and not s(0)) or 
         (not s(3) and not s(2) and s(1)) or 
         (s(3) and s(1) and not s(0)) or 
         (s(2) and not s(1) and not s(0)) or 
         (s(3) and not s(1)) or 
         (s(2) and s(1) and s(0)) or 
         (s(2) and s(1) and not s(0));

    -- Atribuição para a saída e
    e <= (not s(2) and not s(0)) or 
         (s(1) and not s(0)) or 
         (s(3) and s(1)) or 
         (s(3) and s(2));

    -- Atribuição para a saída f
    f <= (not s(1) and not s(0)) or 
         (not s(3) and s(2) and not s(1)) or 
         (s(2) and not s(0)) or 
         (s(3) and not s(2)) or 
         (s(3) and s(1));

    -- Atribuição para a saída g
    g <= (not s(2) and s(1)) or 
         (s(3) and not s(2)) or 
         (s(3) and s(2) and not s(1)) or 
         (s(3) and s(2) and not s(0)) or 
         (s(2) and not s(1) and s(0)) or 
         (s(1) and not s(0)) or 
         (s(3) and s(0));

end Behavioral;
