import unittest

from testing.matematika_test import (
    TestKonversi,
    TestKelilingLingkaran,
    TestDiameterLingkaran,
    TestPersamaanKuadrat,
    TestRataRata,
    TestFaktorial,
    TestPermutasi,
    TestKombinasi,
    TestFPB,
    TestFaktorPrima,
    TestMatriksTranspose,
    TestFungsiEuler,
    TestSigmoid,
    TestDistribusiBinomial,
    TestGaussian,
)

from testing.fisika_test import (
    TestKecepatan,
    TestPercepatan,
    TestGerakLurusBeraturan,
    TestEnergiKinetik,
    TestKetinggianBarometrik,
    TestGayaSentripental,
    TestEfekDoppler,
)

from testing.bilangan_istimewa_test import (
    TestAngkaArmstrong,
    TestAngkaAutomorphic,
    TestAngkaPronic,
    TestAngkaSegitiga,
)

from testing.statistika_test import TestFungsiEntropy, TestFungiStandardDeviasi

if __name__ == "__main__":
    testing_matematika: list = [
        TestKelilingLingkaran,
        TestKonversi,
        TestDiameterLingkaran,
        TestPersamaanKuadrat,
        TestRataRata,
        TestFaktorial,
        TestPermutasi,
        TestKombinasi,
        TestFPB,
        TestFaktorPrima,
        TestMatriksTranspose,
        TestFungsiEuler,
        TestSigmoid,
        TestDistribusiBinomial,
        TestGaussian,
    ]

    testing_fisika: list = [
        TestKecepatan,
        TestPercepatan,
        TestGerakLurusBeraturan,
        TestEnergiKinetik,
        TestKetinggianBarometrik,
        TestGayaSentripental,
        TestEfekDoppler,
    ]

    testing_statistika: list = [
        TestFungsiEntropy,
        TestFungiStandardDeviasi,
    ]

    testing_angka_istimewa: list = [
        TestAngkaArmstrong,
        TestAngkaAutomorphic,
        TestAngkaPronic,
        TestAngkaSegitiga,
    ]

    all_tests = unittest.TestSuite()

    for testing_math in testing_matematika:
        all_tests.addTest(unittest.TestLoader().loadTestsFromTestCase(testing_math))

    for testing_physic in testing_fisika:
        all_tests.addTest(unittest.TestLoader().loadTestsFromTestCase(testing_physic))

    for testing_statistik in testing_statistika:
        all_tests.addTest(
            unittest.TestLoader().loadTestsFromTestCase(testing_statistik)
        )

    for testing_special_number in testing_angka_istimewa:
        all_tests.addTest(
            unittest.TestLoader().loadTestsFromTestCase(testing_special_number)
        )

    unittest.TextTestRunner(verbosity=2).run(all_tests)
