def main() -> None:

    a = int(input("Kérem a kocka oldalának hosszúsagát:"))

    terfogat = a*a*a
    felszin = 6*a*a

    print("A kocka térfogata (V):", terfogat ("m3"))
    print("A kocka felszíne (A):", felszin ("m2"))


if __name__ == "__main__":
    main()
