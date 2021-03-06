#
# PySNMP MIB module HPN-ICF-OID-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HPN-ICF-OID-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:24:56 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, IpAddress, MibIdentifier, enterprises, iso, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Unsigned32, Integer32, ModuleIdentity, Gauge32, Counter32, ObjectIdentity, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "IpAddress", "MibIdentifier", "enterprises", "iso", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Unsigned32", "Integer32", "ModuleIdentity", "Gauge32", "Counter32", "ObjectIdentity", "Bits")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
hp = MibIdentifier((1, 3, 6, 1, 4, 1, 11))
nm = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2))
icf = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14))
hpicfObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11))
hpnicf = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15))
hpnicfCommon = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2))
hpnicfEntityVendorTypeOID = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 3))
hpnicfNM = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 4))
hpnicfSystem = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 6))
hpnicfSNMPAgCpb = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 7))
hpnicfRhw = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8))
hpnicfFtm = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 1))
hpnicfUIMgt = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 2))
hpnicfSystemMan = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 3))
hpnicfConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 4))
hpnicfFlash = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 5))
hpnicfEntityExtend = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 6))
hpnicfIPSecMonitor = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 7))
hpnicfAcl = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 8))
hpnicfVoiceVlan = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 9))
hpnicfL4Redirect = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 10))
hpnicfIpPBX = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 11))
hpnicfUser = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 12))
hpnicfRadius = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 13))
hpnicfPowerEthernetExt = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 14))
hpnicfEntityRelation = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 15))
hpnicfProtocolVlan = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 16))
hpnicfQosProfile = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 17))
hpnicfNat = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 18))
hpnicfPos = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 19))
hpnicfNS = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 20))
hpnicfAAL5 = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 21))
hpnicfSSH = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 22))
hpnicfRSA = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 23))
hpnicfVrrpExt = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 24))
hpnicfIpa = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 25))
hpnicfPortSecurity = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 26))
hpnicfVpls = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 27))
hpnicfE1 = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 28))
hpnicfT1 = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 29))
hpnicfIKEMonitor = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 30))
hpnicfWebSwitch = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 31))
hpnicfAutoDetect = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 32))
hpnicfIpBroadcast = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 33))
hpnicfIpx = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 34))
hpnicfIPS = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 35))
hpnicfDhcpSnoop = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 36))
hpnicfProtocolPriority = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 37))
hpnicfTrap = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 38))
hpnicfVoice = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 39))
hpnicfIfExt = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 40))
hpnicfCfCard = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 41))
hpnicfEpon = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42))
hpnicfDldp = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 43))
hpnicfUnicast = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 44))
hpnicfRrpp = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 45))
hpnicfDomain = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 46))
hpnicfIds = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 47))
hpnicfRcr = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 48))
hpnicfAtmDxi = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 49))
hpnicfMulticast = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 50))
hpnicfMpm = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 51))
hpnicfOadp = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 52))
hpnicfTunnel = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 53))
hpnicfGre = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 54))
hpnicfObjectInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 55))
hpnicfStorage = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 56))
hpnicfDvpn = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 57))
hpnicfDhcpRelay = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 58))
hpnicfIsis = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 59))
hpnicfRpr = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 60))
hpnicfSubnetVlan = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 61))
hpnicfDlswExt = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 62))
hpnicfSyslog = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 63))
hpnicfFlowTemplate = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 64))
hpnicfQos2 = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65))
hpnicfStormConstrain = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 66))
hpnicfIpAddrMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 67))
hpnicfMirrGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 68))
hpnicfQINQ = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 69))
hpnicfTransceiver = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 70))
hpnicfIpv6AddrMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 71))
hpnicfBfdMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 72))
hpnicfRCP = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 73))
hpnicfAcfp = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 74))
hpnicfDot11 = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75))
hpnicfE1T1VI = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 76))
hpnicfL2VpnPwe3 = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 78))
hpnicfMplsOam = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 79))
hpnicfMplsOamPs = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 80))
hpnicfSiemMib = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 81))
hpnicfUps = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 82))
hpnicfEOCCommon = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 83))
hpnicfHPEOC = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 84))
hpnicfAFC = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 85))
hpnicfMultCDR = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 86))
hpnicfMACInformation = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 87))
hpnicfFireWall = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 88))
hpnicfDSP = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 89))
hpnicfNetMan = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 90))
hpnicfStack = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 91))
hpnicfPosa = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 92))
hpnicfWebAuthentication = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 93))
hpnicfCATVTransceiver = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 94))
hpnicfLpbkdt = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 95))
hpnicfMultiMedia = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 96))
hpnicfDns = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 97))
hpnicf3GModem = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 98))
hpnicfPortal = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 99))
hpnicflldp = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 100))
hpnicfDHCPServer = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 101))
hpnicfPPPoEServer = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 102))
hpnicfL2Isolate = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 103))
hpnicfSnmpExt = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 104))
hpnicfVsi = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 105))
hpnicfEvc = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 106))
hpnicfMinm = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 107))
hpnicfBlg = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 108))
hpnicfRS485 = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 109))
hpnicfARPRatelimit = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 110))
hpnicfLI = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 111))
hpnicfDar = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 112))
hpnicfPBR = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 113))
hpnicfAAANasId = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 114))
hpnicfTeTunnel = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 115))
hpnicfLB = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 116))
hpnicfDldp2 = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 117))
hpnicfWIPS = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 118))
hpnicfInfoCenter = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 119))
hpnicfFCoE = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 120))
hpnicfTRNG2 = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 121))
hpnicfDhcp4 = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 122))
hpnicfDhcpSnoop2 = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 124))
hpnicfRmonExt = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 125))
hpnicfIPsecMonitorV2 = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 126))
hpnicfSan = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127))
hpnicfSpb = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 128))
hpnicfPex = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 129))
hpnicfSlbg = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 130))
hpnicfEvi = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 132))
hpnicfIssuUpgrade = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 133))
hpnicfEvb = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 134))
hpnicfFcoeMode = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 135))
hpnicfMDC = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 136))
hpnicfQinQv2 = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 137))
hpnicfVmap = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 138))
hpnicfL2tp = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 139))
hpnicfMultilinkPPPV2 = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 140))
hpnicfLocAAASrv = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 141))
hpnicfMplsExt = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 142))
hpnicfMplsTe = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 143))
hpnicfBpa = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 144))
hpnicfLicense = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 145))
hpnicfARPSourceSuppression = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 146))
hpnicfLBv2 = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 148))
hpnicfSession = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 149))
hpnicfVxlan = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 150))
hpnicfRddc = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 151))
hpnicfIpRanDcn = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 152))
hpnicfContext = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 154))
hpnicfIfQos2 = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1))
hpnicfCBQos2 = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 2))
hpnicfQosCapability = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 7, 1))
hpnicfDHCPRelayMib = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 1))
hpnicfDHCPServerMib = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 2))
hpnicfNqa = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 3))
hpnicfrmonExtend = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 4))
hpnicfpaeExtMib = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 6))
hpnicfHgmp = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 7))
hpnicfDevice = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 8))
hpnicfMpls = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12))
hpnicfTRNG = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 13))
hpnicfUserLogMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 18))
hpnicfNTP = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 22))
hpnicfLAG = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 25))
hpnicfSmonExtend = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 26))
hpnicfQoS = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 32))
hpnicfMultilinkPPP = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 33))
hpnicflswCommon = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35))
hpnicfMplsLsr = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 1))
hpnicfMplsLdp = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 2))
hpnicfMplsVpn = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 12, 3))
hpnicfLswExtInterface = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 1))
hpnicfLswVlan = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 2))
hpnicfLswMacPort = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 3))
hpnicfLswArpMib = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 4))
hpnicfLswL2InfMib = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 5))
hpnicfLswRstpMib = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 6))
hpnicfLswIgmpsnoopingMib = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 7))
hpnicfLswDhcpMib = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 8))
hpnicfLswdevMMib = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 9))
hpnicfLswTrapMib = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 12))
hpnicfdot1sMstp = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 14))
hpnicfLswQosAclMib = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16))
hpnicfLswMix = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 17))
hpnicfLswDeviceAdmin = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 18))
mibBuilder.exportSymbols("HPN-ICF-OID-MIB", hpnicfDHCPServer=hpnicfDHCPServer, hpnicfConfig=hpnicfConfig, hpnicfRadius=hpnicfRadius, hpnicfPowerEthernetExt=hpnicfPowerEthernetExt, hpnicfAFC=hpnicfAFC, hpnicfRS485=hpnicfRS485, hpnicfVoice=hpnicfVoice, hpnicfMplsExt=hpnicfMplsExt, hpnicfQINQ=hpnicfQINQ, hpnicfNqa=hpnicfNqa, nm=nm, hpnicfL2Isolate=hpnicfL2Isolate, hpnicfIpa=hpnicfIpa, hpnicfLswDhcpMib=hpnicfLswDhcpMib, hpnicfAutoDetect=hpnicfAutoDetect, hpnicfRmonExt=hpnicfRmonExt, hpnicfProtocolPriority=hpnicfProtocolPriority, hpnicfPex=hpnicfPex, hpnicfMplsTe=hpnicfMplsTe, hpnicfFcoeMode=hpnicfFcoeMode, hpnicfAAANasId=hpnicfAAANasId, hpnicfLswMacPort=hpnicfLswMacPort, hpnicfFlash=hpnicfFlash, hpnicfRhw=hpnicfRhw, hpnicfMDC=hpnicfMDC, hpnicfSystemMan=hpnicfSystemMan, hpnicfCommon=hpnicfCommon, hpnicfSSH=hpnicfSSH, hpnicfSyslog=hpnicfSyslog, hpnicfPPPoEServer=hpnicfPPPoEServer, hpnicfIPsecMonitorV2=hpnicfIPsecMonitorV2, hpnicfRpr=hpnicfRpr, hpnicfVrrpExt=hpnicfVrrpExt, hpnicfL2tp=hpnicfL2tp, hpnicfTRNG=hpnicfTRNG, hpnicfSession=hpnicfSession, hpnicfTRNG2=hpnicfTRNG2, hpnicfLswTrapMib=hpnicfLswTrapMib, hpnicfAcl=hpnicfAcl, hpnicfLB=hpnicfLB, hpnicfLswMix=hpnicfLswMix, hpnicfMultilinkPPPV2=hpnicfMultilinkPPPV2, hpnicfSlbg=hpnicfSlbg, hpnicfIpAddrMIB=hpnicfIpAddrMIB, hpnicfpaeExtMib=hpnicfpaeExtMib, hpnicfQos2=hpnicfQos2, hpnicfAtmDxi=hpnicfAtmDxi, hpnicfEpon=hpnicfEpon, hpnicfDldp2=hpnicfDldp2, hpnicfDHCPServerMib=hpnicfDHCPServerMib, hpnicfIpv6AddrMIB=hpnicfIpv6AddrMIB, hpnicfDlswExt=hpnicfDlswExt, hpnicfIssuUpgrade=hpnicfIssuUpgrade, hpnicfPortSecurity=hpnicfPortSecurity, hpnicfSan=hpnicfSan, hpnicfHPEOC=hpnicfHPEOC, hpnicfPosa=hpnicfPosa, hpnicfSubnetVlan=hpnicfSubnetVlan, hpnicfLswL2InfMib=hpnicfLswL2InfMib, hp=hp, hpnicfDSP=hpnicfDSP, hpnicfEntityExtend=hpnicfEntityExtend, hpnicfLpbkdt=hpnicfLpbkdt, hpnicfLswExtInterface=hpnicfLswExtInterface, hpnicfDot11=hpnicfDot11, hpnicfMultilinkPPP=hpnicfMultilinkPPP, hpnicfRrpp=hpnicfRrpp, hpnicfContext=hpnicfContext, hpnicfDomain=hpnicfDomain, hpnicfRddc=hpnicfRddc, hpnicfDhcpRelay=hpnicfDhcpRelay, hpnicfMplsLsr=hpnicfMplsLsr, hpnicfUps=hpnicfUps, hpnicfE1=hpnicfE1, hpnicfE1T1VI=hpnicfE1T1VI, hpnicfLicense=hpnicfLicense, hpnicfMplsOam=hpnicfMplsOam, hpnicf=hpnicf, hpnicfStorage=hpnicfStorage, hpnicfObjectInfo=hpnicfObjectInfo, hpnicfIds=hpnicfIds, hpnicfLswRstpMib=hpnicfLswRstpMib, hpnicfLswdevMMib=hpnicfLswdevMMib, hpnicfVsi=hpnicfVsi, hpnicfLswQosAclMib=hpnicfLswQosAclMib, hpnicfdot1sMstp=hpnicfdot1sMstp, hpnicfEOCCommon=hpnicfEOCCommon, hpnicfNS=hpnicfNS, hpnicfMultCDR=hpnicfMultCDR, hpnicfDns=hpnicfDns, hpnicfMpls=hpnicfMpls, hpnicfLswArpMib=hpnicfLswArpMib, hpnicfDldp=hpnicfDldp, hpnicfPBR=hpnicfPBR, hpnicfVxlan=hpnicfVxlan, hpnicfDevice=hpnicfDevice, hpnicfUnicast=hpnicfUnicast, hpnicfCfCard=hpnicfCfCard, hpnicfBpa=hpnicfBpa, hpnicfNat=hpnicfNat, hpnicfSnmpExt=hpnicfSnmpExt, hpnicfLswVlan=hpnicfLswVlan, hpnicfARPSourceSuppression=hpnicfARPSourceSuppression, hpnicfLBv2=hpnicfLBv2, hpnicfUser=hpnicfUser, hpnicfEntityRelation=hpnicfEntityRelation, hpnicfSNMPAgCpb=hpnicfSNMPAgCpb, hpnicfWIPS=hpnicfWIPS, hpnicfFireWall=hpnicfFireWall, hpnicfBfdMIB=hpnicfBfdMIB, hpnicfNetMan=hpnicfNetMan, hpnicfIPS=hpnicfIPS, hpnicfDhcpSnoop2=hpnicfDhcpSnoop2, hpnicfIPSecMonitor=hpnicfIPSecMonitor, hpnicfMplsVpn=hpnicfMplsVpn, hpnicfVmap=hpnicfVmap, hpnicfMplsOamPs=hpnicfMplsOamPs, hpnicfIpx=hpnicfIpx, hpnicfSmonExtend=hpnicfSmonExtend, hpnicfIpPBX=hpnicfIpPBX, hpnicfAAL5=hpnicfAAL5, hpnicfRcr=hpnicfRcr, hpnicfIfExt=hpnicfIfExt, hpnicfCATVTransceiver=hpnicfCATVTransceiver, hpicfObjects=hpicfObjects, hpnicfLocAAASrv=hpnicfLocAAASrv, hpnicf3GModem=hpnicf3GModem, hpnicfIsis=hpnicfIsis, hpnicfVpls=hpnicfVpls, icf=icf, hpnicfPortal=hpnicfPortal, hpnicfDvpn=hpnicfDvpn, hpnicfMACInformation=hpnicfMACInformation, hpnicfMultiMedia=hpnicfMultiMedia, hpnicfMplsLdp=hpnicfMplsLdp, hpnicfMpm=hpnicfMpm, hpnicfTransceiver=hpnicfTransceiver, hpnicfQoS=hpnicfQoS, hpnicfProtocolVlan=hpnicfProtocolVlan, hpnicfTrap=hpnicfTrap, hpnicfQosCapability=hpnicfQosCapability, hpnicfSpb=hpnicfSpb, hpnicfLswIgmpsnoopingMib=hpnicfLswIgmpsnoopingMib, hpnicfUIMgt=hpnicfUIMgt, hpnicfLI=hpnicfLI, hpnicfOadp=hpnicfOadp, hpnicflswCommon=hpnicflswCommon, hpnicfMirrGroup=hpnicfMirrGroup, hpnicfEvb=hpnicfEvb, hpnicfEvi=hpnicfEvi, hpnicfPos=hpnicfPos, hpnicfMinm=hpnicfMinm, hpnicfFtm=hpnicfFtm, hpnicfIpRanDcn=hpnicfIpRanDcn, hpnicfRCP=hpnicfRCP, hpnicfCBQos2=hpnicfCBQos2, hpnicfVoiceVlan=hpnicfVoiceVlan, hpnicfL2VpnPwe3=hpnicfL2VpnPwe3, hpnicfDHCPRelayMib=hpnicfDHCPRelayMib, hpnicfIKEMonitor=hpnicfIKEMonitor, hpnicfUserLogMIB=hpnicfUserLogMIB, hpnicfQinQv2=hpnicfQinQv2, hpnicfDhcpSnoop=hpnicfDhcpSnoop, hpnicfNTP=hpnicfNTP, hpnicfSiemMib=hpnicfSiemMib, hpnicfRSA=hpnicfRSA, hpnicfLswDeviceAdmin=hpnicfLswDeviceAdmin, hpnicfGre=hpnicfGre, hpnicfAcfp=hpnicfAcfp, hpnicfTeTunnel=hpnicfTeTunnel, hpnicfDhcp4=hpnicfDhcp4, hpnicfDar=hpnicfDar, hpnicfHgmp=hpnicfHgmp, hpnicfSystem=hpnicfSystem, hpnicfT1=hpnicfT1, hpnicfL4Redirect=hpnicfL4Redirect, hpnicfWebAuthentication=hpnicfWebAuthentication, hpnicfLAG=hpnicfLAG, hpnicfEntityVendorTypeOID=hpnicfEntityVendorTypeOID, hpnicfIfQos2=hpnicfIfQos2, hpnicfFCoE=hpnicfFCoE, hpnicfrmonExtend=hpnicfrmonExtend, hpnicfEvc=hpnicfEvc, hpnicfTunnel=hpnicfTunnel, hpnicfStormConstrain=hpnicfStormConstrain, hpnicfARPRatelimit=hpnicfARPRatelimit, hpnicfInfoCenter=hpnicfInfoCenter, hpnicfWebSwitch=hpnicfWebSwitch, hpnicfFlowTemplate=hpnicfFlowTemplate, hpnicfIpBroadcast=hpnicfIpBroadcast, hpnicfBlg=hpnicfBlg, hpnicfStack=hpnicfStack, hpnicfNM=hpnicfNM, hpnicflldp=hpnicflldp, hpnicfMulticast=hpnicfMulticast, hpnicfQosProfile=hpnicfQosProfile)
