from typing import Callable, Optional

import pandas as pd
from pytest import FullCase

from ngi_cpt_correlations.definitions.geo import GEO


def calc_assert(
    analysis_from_excel: FullCase,
    key: str,
    rtol: float = 1e-2,
    atol: float = 1e-4,
    log: bool = False,
    callback: Optional[Callable] = None,
) -> None:
    """Helper function to compare a series from the analysis_from_excel with the expected series"""
    analysis_from_excel.processor.calculate()
    calculation_results = analysis_from_excel.processor.data[key]
    expected_values = analysis_from_excel.expected[key]

    if callback:
        callback()

    if log:
        print("key", key)
        print("results from the calculations\n", calculation_results.head(10))
        print("expected values\n", expected_values.head(10))
        print("results from the calculations\n", calculation_results.tail(10))
        print("expected values\n", expected_values.tail(10))

    pd.testing.assert_series_equal(
        calculation_results, expected_values, check_index=False, check_exact=False, atol=atol, rtol=rtol
    )


#
#
class TestCPTProcessCalculation:
    def test_integrate_lab_profile_calculation(self, analysis_from_excel) -> None:
        calc_assert(analysis_from_excel, GEO.depth.key)
        calc_assert(analysis_from_excel, GEO.wc.key)
        calc_assert(analysis_from_excel, GEO.WP.key)
        calc_assert(analysis_from_excel, GEO.LL.key)
        calc_assert(analysis_from_excel, GEO.Ip.key)
        calc_assert(analysis_from_excel, GEO.St.key)
        calc_assert(analysis_from_excel, GEO.uw.key)
        calc_assert(analysis_from_excel, GEO.u0.key)

    def test_sigVtTotal_calculation(self, analysis_from_excel) -> None:
        calc_assert(
            analysis_from_excel,
            GEO.sigVtTotal.key,
            callback=analysis_from_excel.processor._total_vertical_stress,
        )

    def test_sigVtEff_calculation(self, analysis_from_excel) -> None:
        calc_assert(
            analysis_from_excel,
            GEO.sigVtEff.key,
            callback=analysis_from_excel.processor._effective_vertical_stress,
        )

    def test_differential_pressure_calculation(self, analysis_from_excel) -> None:
        calc_assert(
            analysis_from_excel,
            GEO.u_delta.key,
            callback=analysis_from_excel.processor._differential_pressure,
        )

    def test_differential_pressure_normalized_calculation(self, analysis_from_excel) -> None:
        calc_assert(
            analysis_from_excel,
            GEO.u_delta_norm.key,
            callback=analysis_from_excel.processor._normalized_differential_pressure,
        )

    def test_qt_calculation(self, analysis_from_excel) -> None:
        calc_assert(
            analysis_from_excel,
            GEO.qt.key,
            callback=analysis_from_excel.processor._total_cone_resistance,
        )

    def test_qn_calculation(self, analysis_from_excel) -> None:
        calc_assert(
            analysis_from_excel,
            GEO.qn.key,
            callback=analysis_from_excel.processor._net_cone_resistance,
        )

    def test_Qt_calculation(self, analysis_from_excel) -> None:
        calc_assert(
            analysis_from_excel,
            GEO.Qt.key,
            callback=analysis_from_excel.processor._normalized_cone_resistance,
        )

    def test_Bq_calculation(self, analysis_from_excel) -> None:
        calc_assert(
            analysis_from_excel,
            GEO.Bq.key,
            callback=analysis_from_excel.processor._normalized_pressure,
        )

    def test_Rf_calculation(self, analysis_from_excel) -> None:
        calc_assert(
            analysis_from_excel,
            GEO.Rf.key,
            callback=analysis_from_excel.processor._friction_ratio,
        )

    def test_Fr_calculation(self, analysis_from_excel) -> None:
        calc_assert(
            analysis_from_excel,
            GEO.Fr.key,
            callback=analysis_from_excel.processor._normalized_friction_ratio,
        )

    def test_SBT_calculation(self, analysis_from_excel) -> None:
        calc_assert(
            analysis_from_excel,
            GEO.Ic.key,
            callback=analysis_from_excel.processor._soil_behavior_index,
        )
        calc_assert(
            analysis_from_excel,
            GEO.n.key,
            callback=analysis_from_excel.processor._soil_behavior_exponent,
        )
        calc_assert(
            analysis_from_excel,
            GEO.Qtn.key,
            callback=analysis_from_excel.processor._normalized_cone_resistance_with_n,
        )
        calc_assert(
            analysis_from_excel,
            GEO.Icn.key,
            callback=analysis_from_excel.processor._normalized_soil_behavior_index,
        )
