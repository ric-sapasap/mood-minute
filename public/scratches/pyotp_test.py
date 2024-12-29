import pyotp
import qrcode
import qrcode.image.pil


def main():
    """
    Demonstration of TOTP-based passwordless login, 
    showing a QR code in the terminal for easy import into YubiKey Authenticator.
    """

    # 1. Generate or specify a TOTP secret (Base32).
    #    For a fixed secret, just set SECRET_KEY = "JBSWY3DPEHPK3PXP" (example).
    SECRET_KEY = "JBSWY3DPEHPK3PXP"  # auto-generate a random secret
    # SECRET_KEY = pyotp.random_base32()  # auto-generate a random secret

    print("[INFO] Your TOTP secret (Base32) is:")
    print(SECRET_KEY)
    print()

    # 2. Create a TOTP object from this secret.
    totp = pyotp.TOTP(SECRET_KEY)

    # 3. Build a provisioning URI (like what you see in QR codes)
    #    'name' and 'issuer_name' are shown in the Authenticator app label.
    provisioning_uri = totp.provisioning_uri(
        name="ric-sapasap",
        issuer_name="TestPythonApp"
    )

    print("[INFO] Provisioning URI (if needed to manually copy):")
    print(provisioning_uri)
    print()

    # 4. Generate a QR code in the terminal (ASCII) or a typical image:
    print("[INFO] Scan this QR code with YubiKey Authenticator (or other TOTP app):\n")

    # Create a QR object
    qr = qrcode.QRCode()
    qr.add_data(provisioning_uri)
    qr.make()

    # Print an ASCII-based QR code to the terminal
    qr.print_ascii(invert=True)  # 'invert=True' => black on white

    print(
        "\n[INFO] After scanning, you should see a 6-digit TOTP code in your YubiKey Authenticator app.")

    # 5. Prompt user to enter the TOTP code from YubiKey Authenticator
    user_code = input("\nEnter the 6-digit code here: ").strip()

    # 6. Verify
    if totp.verify(user_code):
        print("\n[SUCCESS] The TOTP code is valid! You are authenticated.\n")
    else:
        print("\n[ERROR] Invalid TOTP code. Authentication failed.\n")


if __name__ == "__main__":
    main()
