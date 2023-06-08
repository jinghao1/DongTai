from typing import Tuple
from typing import Any
from typing import Optional
from dataclasses import dataclass, field
from dataclasses_json import dataclass_json, config
from datetime import datetime
from dateutil.parser import parse

# those Tuple[str] = () is not working
# Since https://github.com/lidatong/dataclasses-json/pull/409
# Be careful with potentially nullable types when using them temporarily.


@dataclass_json
@dataclass
class Reference:
    type: str = ""
    url: str = ""


@dataclass_json
@dataclass
class VulCodes:
    CVE: Tuple[str] = ()
    GHSA: Tuple[str] = ()


@dataclass_json
@dataclass
class VulInfo:
    vul_id: str = ""
    cvss_v3: str = ""
    cwe: Tuple[str] = ()
    title: str = ""
    description: str = ""
    references: Tuple[Reference] = ()
    severity: str = ""
    published_time: Optional[datetime] = field(
        default=None,
        metadata=config(decoder=lambda x: parse(x) if x is not None else None,
                        encoder=lambda x: datetime.isoformat(x)
                        if x is not None else None))
    create_time: datetime = field(default=datetime.now(),
                                  metadata=config(decoder=parse,
                                                  encoder=datetime.isoformat))
    update_time: datetime = field(default=datetime.now(),
                                  metadata=config(decoder=parse,
                                                  encoder=datetime.isoformat))
    change_time: datetime = field(default=datetime.now(),
                                  metadata=config(decoder=parse,
                                                  encoder=datetime.isoformat))


@dataclass_json
@dataclass
class Vul:
    vul_info: VulInfo
    vul_codes: VulCodes
    affected_versions: Tuple[str] = ()
    unaffected_versions: Tuple[str] = ()


@dataclass_json
@dataclass
class PackageVulData:
    vuls: Tuple[Vul] = ()
    affected_versions: Tuple[str] = ()
    unaffected_versions: Tuple[str] = ()


@dataclass_json
@dataclass
class PackageInfo:
    ecosystem: str
    language: str
    name: str
    version: str
    hash: str
    version_publish_time: str = ""
    license: Tuple[str] = ()


@dataclass_json
@dataclass
class PackageVulResponse:
    status: int
    msg: str
    data: PackageVulData


@dataclass_json
@dataclass
class PackageResponse:
    status: int
    msg: str
    data: Tuple[PackageInfo] = tuple()
