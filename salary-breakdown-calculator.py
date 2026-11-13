# Day 38 - 2026-11-13
# Salary Breakdown Calculator
# Apnar gross (mool) beton theke basic, bhata, kata-kati (tax, provident fund)
# ar haate-pawa net beton ber kore dey.
# Chakrijibi, HR, ba jekono betonbhogi manusher jonno kajer.
# Kono external library lage na - shudhu plain Python.


def salary_breakdown(gross_salary, provident_fund_percent=10.0, tax_percent=0.0):
    """Gross monthly salary theke pura breakdown ber kore.

    gross_salary: masik mool beton (taka)
    provident_fund_percent: basic er kototuku PF hishebe katbe (default 10%)
    tax_percent: gross er upor anumanik tax har (default 0%)

    Return kore ekta dictionary: prottek khater taka ar net beton.
    """
    if gross_salary <= 0:
        raise ValueError("Beton 0 er beshi hote hobe.")

    # Bangladeshe sadharonoto basic hoy gross er 60%, baki bhata.
    basic = round(gross_salary * 0.60, 2)
    house_rent = round(gross_salary * 0.25, 2)
    medical = round(gross_salary * 0.10, 2)
    conveyance = round(gross_salary - basic - house_rent - medical, 2)

    provident_fund = round(basic * provident_fund_percent / 100, 2)
    tax = round(gross_salary * tax_percent / 100, 2)
    total_deduction = round(provident_fund + tax, 2)
    net_salary = round(gross_salary - total_deduction, 2)

    return {
        "gross_salary": gross_salary,
        "basic": basic,
        "house_rent": house_rent,
        "medical": medical,
        "conveyance": conveyance,
        "provident_fund": provident_fund,
        "tax": tax,
        "total_deduction": total_deduction,
        "net_salary": net_salary,
    }


def show_breakdown(gross_salary, provident_fund_percent=10.0, tax_percent=0.0):
    """Breakdown ta sundor kore print kore."""
    result = salary_breakdown(gross_salary, provident_fund_percent, tax_percent)
    print(f"Gross Salary      : {result['gross_salary']:,.2f} taka")
    print(f"  Basic (60%)     : {result['basic']:,.2f} taka")
    print(f"  House Rent (25%): {result['house_rent']:,.2f} taka")
    print(f"  Medical (10%)   : {result['medical']:,.2f} taka")
    print(f"  Conveyance (5%) : {result['conveyance']:,.2f} taka")
    print(f"Kata-kati:")
    print(f"  Provident Fund  : -{result['provident_fund']:,.2f} taka")
    print(f"  Tax             : -{result['tax']:,.2f} taka")
    print(f"Mot kata          : -{result['total_deduction']:,.2f} taka")
    print(f"Net Salary (haate): {result['net_salary']:,.2f} taka")
    return result


if __name__ == "__main__":
    # Example 1: 50,000 taka beton, 10% PF, kono tax na
    print("Example 1: 50,000 taka beton")
    show_breakdown(50000)

    # Example 2: 80,000 taka beton, 10% PF, 5% anumanik tax
    print("\nExample 2: 80,000 taka beton, 5% tax")
    show_breakdown(80000, tax_percent=5.0)

    # Example 3: 30,000 taka beton, 5% PF
    print("\nExample 3: 30,000 taka beton, 5% PF")
    show_breakdown(30000, provident_fund_percent=5.0)
