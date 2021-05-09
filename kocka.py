def main() -> None:

    a = int(input("Kérem a kocka oldalának hosszúsagát:"))

    terfogat = a*a*a
    felszin = 6*a*a

    print("A kocka térfogata (V):", terfogat)
    print("A kocka felszíne (A):", felszin)


if __name__ == "__main__":
    main()
