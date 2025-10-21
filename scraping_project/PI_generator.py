import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')

# ==============================================================================
# PARAMETRY DO ZMIANY
# ==============================================================================

STEPS = 1000000  # Liczba losowych punktów do wygenerowania
POKAZUJ_WIZUALIZACJE = False # Czy pokazać wykresy (True/False)

# Ustawienia zakresu dla wykresu zbieżności (wykres 2)
AUTOMATYCZNY_ZAKRES = True  # Jeśli True, osie ustawią się automatycznie
# Jeśli False, użyje poniższych wartości

# Zakresy osi - używane tylko gdy AUTOMATYCZNY_ZAKRES = False
OS_X_MIN = 0  # Minimalna wartość na osi X (liczba iteracji)
OS_X_MAX = 100000  # Maksymalna wartość na osi X (liczba iteracji)
OS_Y_MIN = 2.9  # Minimalna wartość na osi Y (wartość π)
OS_Y_MAX = 3.2  # Maksymalna wartość na osi Y (wartość π)

# ==============================================================================
# OBLICZANIE LICZBY PI
# ==============================================================================

# Generowanie losowych współrzędnych x i y w zakresie od -1 do 1
x = np.random.uniform(-1, 1, STEPS)
y = np.random.uniform(-1, 1, STEPS)

# Obliczanie odległości każdego punktu od środka (0, 0)
# Używamy wzoru Pitagorasa: odległość² = x² + y²
odleglosci = x ** 2 + y ** 2

# Sprawdzamy które punkty są wewnątrz okręgu
# Punkt jest wewnątrz gdy jego odległość od środka <= 1
wewnatrz = odleglosci <= 1

# Zliczamy punkty
punkty_wewnatrz = np.sum(wewnatrz)
punkty_na_zewnatrz = STEPS - punkty_wewnatrz

# Obliczamy wartość PI
# Stosunek: pole koła / pole kwadratu = π/4
# Więc: π = 4 * (punkty w kole / wszystkie punkty)
pi_obliczone = 4 * punkty_wewnatrz / STEPS

# Wyświetlamy wyniki
print("=" * 60)
print("OBLICZANIE WARTOŚCI π METODĄ MONTE CARLO")
print("=" * 60)
print(f"Liczba iteracji: {STEPS:,}")
print(f"Punkty wewnątrz okręgu: {punkty_wewnatrz:,}")
print(f"Punkty na zewnątrz okręgu: {punkty_na_zewnatrz:,}")
print()
print(f"Wyznaczona wartość π: {pi_obliczone:.8f}")
print(f"Rzeczywista wartość π: {np.pi:.8f}")
print(f"Błąd bezwzględny: {abs(pi_obliczone - np.pi):.8f}")
print(f"Błąd względny: {abs(pi_obliczone - np.pi) / np.pi * 100:.4f}%")
print("=" * 60)

# ==============================================================================
# WIZUALIZACJA
# ==============================================================================

if POKAZUJ_WIZUALIZACJE:
    # Pokazujemy wszystkie punkty
    ile_punktow_na_wykresie = STEPS

    # Używamy wszystkich punktów do wizualizacji
    x_do_wykresu = x
    y_do_wykresu = y
    wewnatrz_do_wykresu = wewnatrz

    # Tworzymy okno z trzema wykresami
    fig = plt.figure(figsize=(18, 6))
    wykres1 = plt.subplot(1, 3, 1)
    wykres2 = plt.subplot(1, 3, 2)
    wykres3 = plt.subplot(1, 3, 3)

    # ==============================================================================
    # WYKRES 1: Rozkład punktów
    # ==============================================================================

    # Rysujemy punkty wewnątrz okręgu (czerwone)
    wykres1.scatter(x_do_wykresu[wewnatrz_do_wykresu],
                    y_do_wykresu[wewnatrz_do_wykresu],
                    c='red', s=1, alpha=0.5, label='Wewnątrz okręgu')

    # Rysujemy punkty na zewnątrz okręgu (zielone)
    wykres1.scatter(x_do_wykresu[~wewnatrz_do_wykresu],
                    y_do_wykresu[~wewnatrz_do_wykresu],
                    c='green', s=1, alpha=0.5, label='Na zewnątrz okręgu')

    # Rysujemy okrąg
    okrag = plt.Circle((0, 0), 1, fill=False, color='blue', linewidth=2)
    wykres1.add_patch(okrag)

    # Rysujemy osie układu współrzędnych
    wykres1.axhline(y=0, color='black', linewidth=0.5)
    wykres1.axvline(x=0, color='black', linewidth=0.5)

    # Ustawienia wykresu 1
    wykres1.set_xlim(-1.1, 1.1)
    wykres1.set_ylim(-1.1, 1.1)
    wykres1.set_aspect('equal')
    wykres1.grid(True, alpha=0.3)
    wykres1.legend(loc='upper right')
    wykres1.set_title(f'Metoda Monte Carlo\n{ile_punktow_na_wykresie:,} punktów',
                      fontsize=12, fontweight='bold')
    wykres1.set_xlabel('x')
    wykres1.set_ylabel('y')

    # ==============================================================================
    # WYKRES 2: Jak wartość π zmienia się w czasie
    # ==============================================================================

    # Liczymy jak wartość π zmienia się z każdym kolejnym punktem
    kroki = np.arange(1, STEPS + 1)
    suma_wewnatrz = np.cumsum(wewnatrz)
    wartosci_pi = 4 * suma_wewnatrz / kroki

    # Pokazujemy wszystkie punkty
    co_ile = 1

    # Rysujemy linię pokazującą jak π się zmienia
    wykres2.plot(kroki, wartosci_pi,
                 'b-', linewidth=1, alpha=0.7)

    # Rysujemy linię prawdziwej wartości π
    wykres2.axhline(y=np.pi, color='red', linestyle='--',
                    linewidth=2, label=f'π = {np.pi:.6f}')

    # Zamalowujemy obszar między naszą wartością a prawdziwą
    wykres2.fill_between(kroki,
                         wartosci_pi, np.pi,
                         alpha=0.2)

    # Ustawienia wykresu 2
    wykres2.set_xlabel('Liczba iteracji')
    wykres2.set_ylabel('Oszacowana wartość π')
    wykres2.set_title('Zbieżność do prawdziwej wartości π',
                      fontsize=12, fontweight='bold')
    wykres2.legend()
    wykres2.grid(True, alpha=0.3)

    # Ustawienie zakresu osi dla wykresu zbieżności
    if not AUTOMATYCZNY_ZAKRES:
        wykres2.set_xlim(OS_X_MIN, OS_X_MAX)
        wykres2.set_ylim(OS_Y_MIN, OS_Y_MAX)
        print(f"\nUżyto ręcznych zakresów osi dla wykresu zbieżności:")
        print(f"  Oś X (iteracje): {OS_X_MIN} - {OS_X_MAX}")
        print(f"  Oś Y (wartość π): {OS_Y_MIN} - {OS_Y_MAX}")
    else:
        print("\nUżyto automatycznych zakresów osi dla wykresu zbieżności")

    # ==============================================================================
    # WYKRES 3: Błąd RMS (Root Mean Square Error)
    # ==============================================================================

    # Obliczamy błąd dla każdego kroku
    # Błąd = |obliczona wartość π - prawdziwa wartość π|
    bledy = np.abs(wartosci_pi - np.pi)

    # Obliczamy błąd RMS (Root Mean Square)
    # RMS = √(średnia z kwadratów błędów)
    bledy_kwadrat = bledy ** 2
    suma_bledow_kwadrat = np.cumsum(bledy_kwadrat)
    blad_rms = np.sqrt(suma_bledow_kwadrat / kroki)

    # Pokazujemy wszystkie punkty
    wykres3.plot(kroki, blad_rms,
                 'purple', linewidth=2, alpha=0.7, label='Błąd RMS')

    # Dodajemy linię pomocniczą przy 0
    wykres3.axhline(y=0, color='red', linestyle='--',
                    linewidth=1, alpha=0.5, label='Brak błędu')

    # Ustawienia wykresu 3
    wykres3.set_xlabel('Liczba iteracji')
    wykres3.set_ylabel('Błąd RMS')
    wykres3.set_title('Błąd RMS wyznaczonej wartości π',
                      fontsize=12, fontweight='bold')
    wykres3.legend()
    wykres3.grid(True, alpha=0.3)

    # Opcjonalnie ustawiamy zakres osi
    if not AUTOMATYCZNY_ZAKRES:
        wykres3.set_xlim(OS_X_MIN, OS_X_MAX)

    # Dodajemy informację o końcowym błędzie RMS
    koncowy_blad_rms = blad_rms[-1]
    wykres3.text(0.98, 0.98, f'Końcowy błąd RMS:\n{koncowy_blad_rms:.6f}',
                 transform=wykres3.transAxes,
                 verticalalignment='top',
                 horizontalalignment='right',
                 bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5),
                 fontsize=10)

    # Pokazujemy wykresy
    plt.tight_layout()
    plt.show()

print("\nProgram zakończony!")