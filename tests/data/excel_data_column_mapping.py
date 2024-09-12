from dataclasses import dataclass, field

from ngi_calculations.cpt_correlations.definitions.geo import GEO


@dataclass(frozen=True)
class CptRawColumns:
    columns: dict = field(
        default_factory=lambda: {
            "A": GEO.depth.key,
            "B": GEO.qc.key,
            "C": GEO.fs.key,
            "D": GEO.u2.key,
            "E": GEO.temperature.key,
            "F": GEO.penetration_rate.key,
            "G": GEO.penetration_force.key,
            "H": GEO.tilt.key,
        }
    )


@dataclass(frozen=True)
class LabDataColumns:
    columns: dict = field(
        default_factory=lambda: {
            "A": GEO.depth.key,
            "B": GEO.wc.key,
            "C": GEO.WP.key,
            "D": GEO.LL.key,
            "E": GEO.Ip.key,
            "F": GEO.St.key,
            "G": GEO.uw.key,
            "H": GEO.u0.key,
        }
    )


@dataclass(frozen=True)
class CptProcessedColumns:
    columns: dict = field(
        default_factory=lambda: {
            **CptRawColumns().columns,
            "I": GEO.wc.key,
            "J": GEO.WP.key,
            "K": GEO.LL.key,
            "L": GEO.Ip.key,
            "M": GEO.St.key,
            "N": GEO.uw.key,
            "O": GEO.u0.key,
            "P": GEO.sigVtTotal.key,
            "Q": GEO.sigVtEff.key,
            "R": GEO.qt.key,
            "S": GEO.qn.key,
            "T": GEO.u_delta.key,
            "U": GEO.Fr.key,
            "V": GEO.Qt.key,
            "W": GEO.Bq.key,
            "X": GEO.u_delta_norm.key,
            "Y": GEO.Ic.key,
            "Z": GEO.n.key,
            "AA": GEO.Qtn.key,
            "AB": GEO.Icn.key,
            "AC": GEO.Rf.key,
        }
    )
