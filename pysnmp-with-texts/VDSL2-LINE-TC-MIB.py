#
# PySNMP MIB module VDSL2-LINE-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/VDSL2-LINE-TC-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:57:23 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, MibIdentifier, ObjectIdentity, transmission, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, NotificationType, Counter64, IpAddress, Counter32, Bits, iso, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "MibIdentifier", "ObjectIdentity", "transmission", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "NotificationType", "Counter64", "IpAddress", "Counter32", "Bits", "iso", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
vdsl2TCMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 10, 251, 3))
vdsl2TCMIB.setRevisions(('2009-09-30 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: vdsl2TCMIB.setRevisionsDescriptions(('Initial version, published as RFC 5650.',))
if mibBuilder.loadTexts: vdsl2TCMIB.setLastUpdated('200909300000Z')
if mibBuilder.loadTexts: vdsl2TCMIB.setOrganization('ADSLMIB Working Group')
if mibBuilder.loadTexts: vdsl2TCMIB.setContactInfo('WG-email: adslmib@ietf.org Info: https://www1.ietf.org/mailman/listinfo/adslmib Chair: Mike Sneed Sand Channel Systems Postal: P.O. Box 37324 Raleigh NC 27627-732 Email: sneedmike@hotmail.com Phone: +1 206 600 7022 Co-Chair: Menachem Dodge ECI Telecom Ltd. Postal: 30 Hasivim St. Petach Tikva 49517, Israel. Email: mbdodge@ieee.org Phone: +972 3 926 8421 Co-editor: Moti Morgenstern ECI Telecom Ltd. Postal: 30 Hasivim St. Petach Tikva 49517, Israel. Email: moti.morgenstern@ecitele.com Phone: +972 3 926 6258 Co-editor: Scott Baillie NEC Australia Postal: 649-655 Springvale Road, Mulgrave, Victoria 3170, Australia. Email: scott.baillie@nec.com.au Phone: +61 3 9264 3986 Co-editor: Umberto Bonollo NEC Australia Postal: 649-655 Springvale Road, Mulgrave, Victoria 3170, Australia. Email: umberto.bonollo@nec.com.au Phone: +61 3 9264 3385 ')
if mibBuilder.loadTexts: vdsl2TCMIB.setDescription("This MIB Module provides Textual Conventions to be used by the VDSL2-LINE-MIB module for the purpose of managing VDSL2, ADSL, ADSL2, and ADSL2+ lines. Copyright (c) 2009 IETF Trust and the persons identified as authors of the code. All rights reserved. Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met: - Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer. - Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution. - Neither the name of Internet Society, IETF or IETF Trust, nor the names of specific contributors, may be used to endorse or promote products derived from this software without specific prior written permission. THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS 'AS IS' AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE. This version of this MIB module is part of RFC 5650; see the RFC itself for full legal notices.")
class Xdsl2Unit(TextualConvention, Integer32):
    description = 'Identifies a transceiver as being either xTU-C or xTU-R. A VDSL2/ADSL/ADSL2 or ADSL2+ line consists of two transceivers: an xTU-C and an xTU-R. In the case of ADSL/ADSL2 and ADSL2+, those two transceivers are also called atuc and atur. In the case of VDSL2, those two transceivers are also called vtuc and vtur. Specified as an INTEGER, the two values are: xtuc(1) -- central office transceiver xtur(2) -- remote site transceiver'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("xtuc", 1), ("xtur", 2))

class Xdsl2Direction(TextualConvention, Integer32):
    description = 'Identifies the direction of a band in a VDSL2/ADSL/ADSL2/ ADSL2+ link. The upstream direction is a transmission from the remote end (xTU-R) towards the central office end (xTU-C). The downstream direction is a transmission from the xTU-C towards the xTU-R. Specified as an INTEGER, the values are defined as follows:'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("upstream", 1), ("downstream", 2))

class Xdsl2Band(TextualConvention, Integer32):
    description = 'Identifies a band in a VDSL2/ADSL/ADSL2/ADSL2+ link. For a band in the upstream direction, transmission is from the remote end (xTU-R) towards the central office end (xTU-C). For a band in the downstream direction, transmission is from the xTU-C towards the xTU-R. For ADSL, ADSL2 and ADSL2+, which use a single band in the upstream direction and a single band in the downstream direction, the only relevant values are upstream(1) and downstream(2). For VDSL2, which uses multiple bands in each transmission direction, a band in the upstream direction is indicated by any of us0(3), us1(5), us2(7), us3(9), or us4(11), and a band in the downstream direction is indicated by any of ds1(4), ds2(6), ds3(8), or ds4(10). For VDSL2, the values upstream(1) and downstream(2) may be used when there is a need to refer to the whole upstream or downstream traffic (e.g., report the average signal-to-noise ratio on any transmission direction). Specified as an INTEGER, the values are defined as follows:'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))
    namedValues = NamedValues(("upstream", 1), ("downstream", 2), ("us0", 3), ("ds1", 4), ("us1", 5), ("ds2", 6), ("us2", 7), ("ds3", 8), ("us3", 9), ("ds4", 10), ("us4", 11))

class Xdsl2TransmissionModeType(TextualConvention, Bits):
    description = 'A set of xDSL line transmission modes, with one bit per mode. The notes (F) and (L) denote Full-Rate and Lite/splitterless, respectively: Bit 00 : Regional Std. (ANSI T1.413) (F) Bit 01 : Regional Std. (ETSI DTS/TM06006) (F) Bit 02 : G.992.1 POTS non-overlapped (F) Bit 03 : G.992.1 POTS overlapped (F) Bit 04 : G.992.1 ISDN non-overlapped (F) Bit 05 : G.992.1 ISDN overlapped (F) Bit 06 : G.992.1 TCM-ISDN non-overlapped (F) Bit 07 : G.992.1 TCM-ISDN overlapped (F) Bit 08 : G.992.2 POTS non-overlapped (L) Bit 09 : G.992.2 POTS overlapped (L) Bit 10 : G.992.2 with TCM-ISDN non-overlapped (L) Bit 11 : G.992.2 with TCM-ISDN overlapped (L) Bit 12 : G.992.1 TCM-ISDN symmetric (F) --- not in G.997.1 Bit 13-17: Reserved Bit 18 : G.992.3 POTS non-overlapped (F) Bit 19 : G.992.3 POTS overlapped (F) Bit 20 : G.992.3 ISDN non-overlapped (F) Bit 21 : G.992.3 ISDN overlapped (F) Bit 22-23: Reserved Bit 24 : G.992.4 POTS non-overlapped (L) Bit 25 : G.992.4 POTS overlapped (L) Bit 26-27: Reserved Bit 28 : G.992.3 Annex I All-Digital non-overlapped (F) Bit 29 : G.992.3 Annex I All-Digital overlapped (F) Bit 30 : G.992.3 Annex J All-Digital non-overlapped (F) Bit 31 : G.992.3 Annex J All-Digital overlapped (F) Bit 32 : G.992.4 Annex I All-Digital non-overlapped (L) Bit 33 : G.992.4 Annex I All-Digital overlapped (L) Bit 34 : G.992.3 Annex L POTS non-overlapped, mode 1, wide U/S (F) Bit 35 : G.992.3 Annex L POTS non-overlapped, mode 2, narrow U/S(F) Bit 36 : G.992.3 Annex L POTS overlapped, mode 3, wide U/S (F) Bit 37 : G.992.3 Annex L POTS overlapped, mode 4, narrow U/S (F) Bit 38 : G.992.3 Annex M POTS non-overlapped (F) Bit 39 : G.992.3 Annex M POTS overlapped (F) Bit 40 : G.992.5 POTS non-overlapped (F) Bit 41 : G.992.5 POTS overlapped (F) Bit 42 : G.992.5 ISDN non-overlapped (F) Bit 43 : G.992.5 ISDN overlapped (F) Bit 44-45: Reserved Bit 46 : G.992.5 Annex I All-Digital non-overlapped (F) Bit 47 : G.992.5 Annex I All-Digital overlapped (F) Bit 48 : G.992.5 Annex J All-Digital non-overlapped (F) Bit 49 : G.992.5 Annex J All-Digital overlapped (F) Bit 50 : G.992.5 Annex M POTS non-overlapped (F) Bit 51 : G.992.5 Annex M POTS overlapped (F) Bit 52-55: Reserved Bit 56 : G.993.2 Annex A Bit 57 : G.993.2 Annex B Bit 58 : G.993.2 Annex C Bit 59-63: Reserved'
    status = 'current'
    namedValues = NamedValues(("ansit1413", 0), ("etsi", 1), ("g9921PotsNonOverlapped", 2), ("g9921PotsOverlapped", 3), ("g9921IsdnNonOverlapped", 4), ("g9921isdnOverlapped", 5), ("g9921tcmIsdnNonOverlapped", 6), ("g9921tcmIsdnOverlapped", 7), ("g9922potsNonOverlapped", 8), ("g9922potsOverlapped", 9), ("g9922tcmIsdnNonOverlapped", 10), ("g9922tcmIsdnOverlapped", 11), ("g9921tcmIsdnSymmetric", 12), ("reserved1", 13), ("reserved2", 14), ("reserved3", 15), ("reserved4", 16), ("reserved5", 17), ("g9923PotsNonOverlapped", 18), ("g9923PotsOverlapped", 19), ("g9923IsdnNonOverlapped", 20), ("g9923isdnOverlapped", 21), ("reserved6", 22), ("reserved7", 23), ("g9924potsNonOverlapped", 24), ("g9924potsOverlapped", 25), ("reserved8", 26), ("reserved9", 27), ("g9923AnnexIAllDigNonOverlapped", 28), ("g9923AnnexIAllDigOverlapped", 29), ("g9923AnnexJAllDigNonOverlapped", 30), ("g9923AnnexJAllDigOverlapped", 31), ("g9924AnnexIAllDigNonOverlapped", 32), ("g9924AnnexIAllDigOverlapped", 33), ("g9923AnnexLMode1NonOverlapped", 34), ("g9923AnnexLMode2NonOverlapped", 35), ("g9923AnnexLMode3Overlapped", 36), ("g9923AnnexLMode4Overlapped", 37), ("g9923AnnexMPotsNonOverlapped", 38), ("g9923AnnexMPotsOverlapped", 39), ("g9925PotsNonOverlapped", 40), ("g9925PotsOverlapped", 41), ("g9925IsdnNonOverlapped", 42), ("g9925isdnOverlapped", 43), ("reserved10", 44), ("reserved11", 45), ("g9925AnnexIAllDigNonOverlapped", 46), ("g9925AnnexIAllDigOverlapped", 47), ("g9925AnnexJAllDigNonOverlapped", 48), ("g9925AnnexJAllDigOverlapped", 49), ("g9925AnnexMPotsNonOverlapped", 50), ("g9925AnnexMPotsOverlapped", 51), ("reserved12", 52), ("reserved13", 53), ("reserved14", 54), ("reserved15", 55), ("g9932AnnexA", 56), ("g9932AnnexB", 57), ("g9932AnnexC", 58), ("reserved16", 59), ("reserved17", 60), ("reserved18", 61), ("reserved19", 62), ("reserved20", 63))

class Xdsl2RaMode(TextualConvention, Integer32):
    description = 'Specifies the rate adaptation behavior for the line. The three possible behaviors are: manual (1) - No Rate-Adaptation. The initialization process attempts to synchronize to a specified rate. raInit (2) - Rate-Adaptation during initialization process only, which attempts to synchronize to a rate between minimum and maximum specified values. dynamicRa (3)- Dynamic Rate-Adaptation during initialization process as well as during Showtime.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("manual", 1), ("raInit", 2), ("dynamicRa", 3))

class Xdsl2InitResult(TextualConvention, Integer32):
    description = 'Specifies the result of full initialization attempt; the six possible result values are: noFail (0) - Successful initialization configError (1) - Configuration failure configNotFeasible (2) - Configuration details not supported commFail (3) - Communication failure noPeerAtu (4) - Peer ATU not detected otherCause (5) - Other initialization failure reason'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))
    namedValues = NamedValues(("noFail", 0), ("configError", 1), ("configNotFeasible", 2), ("commFail", 3), ("noPeerAtu", 4), ("otherCause", 5))

class Xdsl2OperationModes(TextualConvention, Integer32):
    description = 'The VDSL2 management model specified includes an xDSL Mode object that identifies an instance of xDSL Mode-Specific PSD Configuration object in the xDSL Line Profile. The following classes of xDSL operating mode are defined. The notes (F) and (L) denote Full-Rate and Lite/splitterless, respectively: +-------+--------------------------------------------------+ | Value | xDSL operation mode description | +-------+--------------------------------------------------+ 1 - The default/generic PSD configuration. Default configuration will be used when no other matching mode-specific configuration can be found. 2 - Regional Std. (ANSI T1.413) (F) 3 - Regional Std. (ETSI DTS/TM06006) (F) 4 - G.992.1 POTS non-overlapped (F) 5 - G.992.1 POTS overlapped (F) 6 - G.992.1 ISDN non-overlapped (F) 7 - G.992.1 ISDN overlapped (F) 8 - G.992.1 TCM-ISDN non-overlapped (F) 9 - G.992.1 TCM-ISDN overlapped (F) 10 - G.992.2 POTS non-overlapped (L) 11 - G.992.2 POTS overlapped (L) 12 - G.992.2 with TCM-ISDN non-overlapped (L) 13 - G.992.2 with TCM-ISDN overlapped (L) 14 - G.992.1 TCM-ISDN symmetric (F) --- not in G.997.1 15-19 - Unused. Reserved for future ITU-T specification. 20 - G.992.3 POTS non-overlapped (F) 21 - G.992.3 POTS overlapped (F) 22 - G.992.3 ISDN non-overlapped (F) 23 - G.992.3 ISDN overlapped (F) 24-25 - Unused. Reserved for future ITU-T specification. 26 - G.992.4 POTS non-overlapped (L) 27 - G.992.4 POTS overlapped (L) 28-29 - Unused. Reserved for future ITU-T specification. 30 - G.992.3 Annex I All-Digital non-overlapped (F) 31 - G.992.3 Annex I All-Digital overlapped (F) 32 - G.992.3 Annex J All-Digital non-overlapped (F) 33 - G.992.3 Annex J All-Digital overlapped (F) 34 - G.992.4 Annex I All-Digital non-overlapped (L) 35 - G.992.4 Annex I All-Digital overlapped (L) 36 - G.992.3 Annex L POTS non-overlapped, mode 1, wide U/S (F) 37 - G.992.3 Annex L POTS non-overlapped, mode 2, narrow U/S(F) 38 - G.992.3 Annex L POTS overlapped, mode 3, wide U/S (F) 39 - G.992.3 Annex L POTS overlapped, mode 4, narrow U/S (F) 40 - G.992.3 Annex M POTS non-overlapped (F) 41 - G.992.3 Annex M POTS overlapped (F) 42 - G.992.5 POTS non-overlapped (F) 43 - G.992.5 POTS overlapped (F) 44 - G.992.5 ISDN non-overlapped (F) 45 - G.992.5 ISDN overlapped (F) 46-47 - Unused. Reserved for future ITU-T specification. 48 - G.992.5 Annex I All-Digital non-overlapped (F) 49 - G.992.5 Annex I All-Digital overlapped (F) 50 - G.992.5 Annex J All-Digital non-overlapped (F) 51 - G.992.5 Annex J All-Digital overlapped (F) 52 - G.992.5 Annex M POTS non-overlapped (F) 53 - G.992.5 Annex M POTS overlapped (F) 54-57 - Unused. Reserved for future ITU-T specification. 58 - G.993.2 Annex A 59 - G.993.2 Annex B 60 - G.993.2 Annex C '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 20, 21, 22, 23, 26, 27, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 48, 49, 50, 51, 52, 53, 58, 59, 60))
    namedValues = NamedValues(("defMode", 1), ("ansit1413", 2), ("etsi", 3), ("g9921PotsNonOverlapped", 4), ("g9921PotsOverlapped", 5), ("g9921IsdnNonOverlapped", 6), ("g9921isdnOverlapped", 7), ("g9921tcmIsdnNonOverlapped", 8), ("g9921tcmIsdnOverlapped", 9), ("g9922potsNonOverlapped", 10), ("g9922potsOverlapped", 11), ("g9922tcmIsdnNonOverlapped", 12), ("g9922tcmIsdnOverlapped", 13), ("g9921tcmIsdnSymmetric", 14), ("g9923PotsNonOverlapped", 20), ("g9923PotsOverlapped", 21), ("g9923IsdnNonOverlapped", 22), ("g9923isdnOverlapped", 23), ("g9924potsNonOverlapped", 26), ("g9924potsOverlapped", 27), ("g9923AnnexIAllDigNonOverlapped", 30), ("g9923AnnexIAllDigOverlapped", 31), ("g9923AnnexJAllDigNonOverlapped", 32), ("g9923AnnexJAllDigOverlapped", 33), ("g9924AnnexIAllDigNonOverlapped", 34), ("g9924AnnexIAllDigOverlapped", 35), ("g9923AnnexLMode1NonOverlapped", 36), ("g9923AnnexLMode2NonOverlapped", 37), ("g9923AnnexLMode3Overlapped", 38), ("g9923AnnexLMode4Overlapped", 39), ("g9923AnnexMPotsNonOverlapped", 40), ("g9923AnnexMPotsOverlapped", 41), ("g9925PotsNonOverlapped", 42), ("g9925PotsOverlapped", 43), ("g9925IsdnNonOverlapped", 44), ("g9925isdnOverlapped", 45), ("g9925AnnexIAllDigNonOverlapped", 48), ("g9925AnnexIAllDigOverlapped", 49), ("g9925AnnexJAllDigNonOverlapped", 50), ("g9925AnnexJAllDigOverlapped", 51), ("g9925AnnexMPotsNonOverlapped", 52), ("g9925AnnexMPotsOverlapped", 53), ("g9932AnnexA", 58), ("g9932AnnexB", 59), ("g9932AnnexC", 60))

class Xdsl2PowerMngState(TextualConvention, Integer32):
    description = 'Objects with this syntax uniquely identify each power management state defined for the VDSL2/ADSL/ADSL2 or ADSL2+ link. In VDSL2, only L0 and L3 states are defined. The possible values are: l0(1) - L0: Full power. Synchronized and full transmission (i.e., Showtime). l1(2) - L1: Low power with reduced net data rate (for G.992.2 only). l2(3) - L2: Low power with reduced net data rate (for G.992.3, G.992.4 and G.992.5). l3(4) - L3: Idle power management state / No power.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("l0", 1), ("l1", 2), ("l2", 3), ("l3", 4))

class Xdsl2ConfPmsForce(TextualConvention, Integer32):
    description = 'Objects with this syntax are configuration parameters that specify the desired power management state transition for the VDSL2/ADSL/ADSL2 or ADSL2+ link. In VDSL2, only L0 and L3 states are defined: l3toL0 (0) - Perform a transition from L3 to L0 (Full power management state). l0toL2 (2) - Perform a transition from L0 to L2 (Low power management state). l0orL2toL3 (3) - Perform a transition into L3 (Idle power management state).'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 2, 3))
    namedValues = NamedValues(("l3toL0", 0), ("l0toL2", 2), ("l0orL2toL3", 3))

class Xdsl2LinePmMode(TextualConvention, Bits):
    description = 'Objects with this syntax are configuration parameters that reference the power modes/states into which the xTU-C or xTU-R may autonomously transit. It is a BITS structure that allows control of the following transit options: allowTransitionsToIdle (0) - xTU may autonomously transit to idle (L3) state. allowTransitionsToLowPower (1)- xTU may autonomously transit to low-power (L1/L2) state.'
    status = 'current'
    namedValues = NamedValues(("allowTransitionsToIdle", 0), ("allowTransitionsToLowPower", 1))

class Xdsl2LineLdsf(TextualConvention, Integer32):
    description = 'Objects with this syntax are configuration parameters that control the Loop Diagnostic mode for a VDSL2/ADSL/ADSL2 or ADSL2+ link. The possible values are: inhibit (0) - Inhibit Loop Diagnostic mode force (1) - Force/Initiate Loop Diagnostic mode'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("inhibit", 0), ("force", 1))

class Xdsl2LdsfResult(TextualConvention, Integer32):
    description = "Possible failure reasons associated with performing Dual Ended Loop Test (DELT) on a DSL line. Possible values are: none (1) - The default value in case LDSF was never requested for the associated line. success (2) - The recent command completed successfully. inProgress (3) - The Loop Diagnostics process is in progress. unsupported (4) - The NE or the line card doesn't support LDSF. cannotRun (5) - The NE cannot initiate the command, due to a nonspecific reason. aborted (6) - The Loop Diagnostics process aborted. failed (7) - The Loop Diagnostics process failed. illegalMode (8) - The NE cannot initiate the command, due to the specific mode of the relevant line. adminUp (9) - The NE cannot initiate the command, as the relevant line is administratively 'Up'. tableFull (10)- The NE cannot initiate the command, due to reaching the maximum number of rows in the results table. noResources (11)- The NE cannot initiate the command, due to lack of internal memory resources."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))
    namedValues = NamedValues(("none", 1), ("success", 2), ("inProgress", 3), ("unsupported", 4), ("cannotRun", 5), ("aborted", 6), ("failed", 7), ("illegalMode", 8), ("adminUp", 9), ("tableFull", 10), ("noResources", 11))

class Xdsl2LineBpsc(TextualConvention, Integer32):
    description = 'Objects with this syntax are configuration parameters that control the bits per subcarrier measurement for a VDSL2/ADSL/ADSL2 or ADSL2+ link. The possible values are: idle (1) - Idle state measure (2) - Measure the bits per subcarrier'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("idle", 1), ("measure", 2))

class Xdsl2BpscResult(TextualConvention, Integer32):
    description = 'Possible failure reasons associated with performing a bits per subcarrier measurement on a DSL line. Possible values are: none (1) - The default value, in case a measurement was never requested for the associated line. success (2) - The recent measurement request completed successfully. inProgress (3) - The bits per subcarrier measurement is in progress. unsupported (4) - The bits per subcarrier request mechanism is not supported. failed (5) - The measurement request has failed and no results are available. noResources (6) - The NE cannot initiate the command, due to lack of internal memory resources.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("none", 1), ("success", 2), ("inProgress", 3), ("unsupported", 4), ("failed", 5), ("noResources", 6))

class Xdsl2LineReset(TextualConvention, Integer32):
    description = 'This type is used to request a line reset to occur. idle (1) - This state indicates that there is currently no request for a line reset. reset (2) - This state indicates that a line reset request has been issued.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("idle", 1), ("reset", 2))

class Xdsl2LineProfiles(TextualConvention, Bits):
    description = 'Objects with this syntax reference the list of ITU-T G.993.2 implementation profiles supported by an xTU, enabled on the VDSL2 line or active on that line.'
    status = 'current'
    namedValues = NamedValues(("profile8a", 0), ("profile8b", 1), ("profile8c", 2), ("profile8d", 3), ("profile12a", 4), ("profile12b", 5), ("profile17a", 6), ("profile30a", 7))

class Xdsl2LineClassMask(TextualConvention, Integer32):
    description = 'VDSL2 PSD Mask Class. The limit Power Spectral Density masks are grouped in the following PSD mask classes: Class 998 Annex A: D-32, D-48, D-64, D-128. Class 997-M1c Annex B: 997-M1c-A-7. Class 997-M1x Annex B: 997-M1x-M-8, 997-M1x-M. Class 997-M2x Annex B: 997-M2x-M-8, 997-M2x-A, 997-M2x-M, 997E17-M2x-NUS0, 997E30-M2x-NUS0. Class 998-M1x Annex B: 998-M1x-A, 998-M1x-B, 998-M1x-NUS0. Class 998-M2x Annex B: 998-M2x-A, 998-M2x-M, 998-M2x-B, 998-M2x-NUS0, 998E17-M2x-NUS0, 998E17-M2x-NUS0-M, 998E30-M2x-NUS0, 998E30-M2x-NUS0-M. Class 998ADE-M2x Annex B: Annex B: 998-M2x-A, 998-M2x-M, 998-M2x-B, 998-M2x-NUS0, 998ADE17-M2x-A, 998ADE17-M2x-B, 998ADE17-M2x-NUS0-M, 998ADE30-M2x-NUS0-A, 998ADE30-M2x-NUS0-M. Class 998-B Annex C: POTS-138b, POTS-276b per C.2.1.1 in G.993.2, TCM-ISDN per C.2.1.2 in G.993.2. Class 998-CO Annex C: POTS-138co, POTS-276co per C.2.1.1 in G.993.2. Class HPE-M1 Annex B: HPE17-M1-NUS0, HPE30-M1-NUS0.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("none", 1), ("a998ORb997M1cORc998B", 2), ("b997M1xOR998co", 3), ("b997M2x", 4), ("b998M1x", 5), ("b998M2x", 6), ("b998AdeM2x", 7), ("bHpeM1", 8))

class Xdsl2LineLimitMask(TextualConvention, Bits):
    description = 'The G.993.2 limit PSD mask for each class of profile. The profiles are grouped in following profile classes: - Class 8: Profiles 8a, 8b, 8c, 8d. - Class 12: Profiles 12a, 12b. - Class 17: Profile 17a. - Class 30: Profile 30a.'
    status = 'current'
    namedValues = NamedValues(("profile8Limit1", 0), ("profile8Limit2", 1), ("profile8Limit3", 2), ("profile8Limit4", 3), ("profile8Limit5", 4), ("profile8Limit6", 5), ("profile8Limit7", 6), ("profile8Limit8", 7), ("profile8Limit9", 8), ("profile8Limit10", 9), ("profile8Limit11", 10), ("profile8Limit12", 11), ("profile8Limit13", 12), ("profile8Limit14", 13), ("profile8Limit15", 14), ("profile8Limit16", 15), ("profile12Limit1", 16), ("profile12Limit2", 17), ("profile12Limit3", 18), ("profile12Limit4", 19), ("profile12Limit5", 20), ("profile12Limit6", 21), ("profile12Limit7", 22), ("profile12Limit8", 23), ("profile12Limit9", 24), ("profile12Limit10", 25), ("profile12Limit11", 26), ("profile12Limit12", 27), ("profile12Limit13", 28), ("profile12Limit14", 29), ("profile12Limit15", 30), ("profile12Limit16", 31), ("profile17Limit1", 32), ("profile17Limit2", 33), ("profile17Limit3", 34), ("profile17Limit4", 35), ("profile17Limit5", 36), ("profile17Limit6", 37), ("profile17Limit7", 38), ("profile17Limit8", 39), ("profile17Limit9", 40), ("profile17Limit10", 41), ("profile17Limit11", 42), ("profile17Limit12", 43), ("profile17Limit13", 44), ("profile17Limit14", 45), ("profile17Limit15", 46), ("profile17Limit16", 47), ("profile30Limit1", 48), ("profile30Limit2", 49), ("profile30Limit3", 50), ("profile30Limit4", 51), ("profile30Limit5", 52), ("profile30Limit6", 53), ("profile30Limit7", 54), ("profile30Limit8", 55), ("profile30Limit9", 56), ("profile30Limit10", 57), ("profile30Limit11", 58), ("profile30Limit12", 59), ("profile30Limit13", 60), ("profile30Limit14", 61), ("profile30Limit15", 62), ("profile30Limit16", 63))

class Xdsl2LineUs0Disable(TextualConvention, Bits):
    description = 'Indicates if US0 is disabled for each limit PSD mask. The profiles are grouped in following profile classes: - Class 8: Profiles 8a, 8b, 8c, 8d. - Class 12: Profiles 12a, 12b. - Class 17: Profile 17a. - Class 30: Profile 30a.'
    status = 'current'
    namedValues = NamedValues(("profile8Us0Disable1", 0), ("profile8Us0Disable2", 1), ("profile8Us0Disable3", 2), ("profile8Us0Disable4", 3), ("profile8Us0Disable5", 4), ("profile8Us0Disable6", 5), ("profile8Us0Disable7", 6), ("profile8Us0Disable8", 7), ("profile8Us0Disable9", 8), ("profile8Us0Disable10", 9), ("profile8Us0Disable11", 10), ("profile8Us0Disable12", 11), ("profile8Us0Disable13", 12), ("profile8Us0Disable14", 13), ("profile8Us0Disable15", 14), ("profile8Us0Disable16", 15), ("profile12Us0Disable1", 16), ("profile12Us0Disable2", 17), ("profile12Us0Disable3", 18), ("profile12Us0Disable4", 19), ("profile12Us0Disable5", 20), ("profile12Us0Disable6", 21), ("profile12Us0Disable7", 22), ("profile12Us0Disable8", 23), ("profile12Us0Disable9", 24), ("profile12Us0Disable10", 25), ("profile12Us0Disable11", 26), ("profile12Us0Disable12", 27), ("profile12Us0Disable13", 28), ("profile12Us0Disable14", 29), ("profile12Us0Disable15", 30), ("profile12Us0Disable16", 31), ("profile17Us0Disable1", 32), ("profile17Us0Disable2", 33), ("profile17Us0Disable3", 34), ("profile17Us0Disable4", 35), ("profile17Us0Disable5", 36), ("profile17Us0Disable6", 37), ("profile17Us0Disable7", 38), ("profile17Us0Disable8", 39), ("profile17Us0Disable9", 40), ("profile17Us0Disable10", 41), ("profile17Us0Disable11", 42), ("profile17Us0Disable12", 43), ("profile17Us0Disable13", 44), ("profile17Us0Disable14", 45), ("profile17Us0Disable15", 46), ("profile17Us0Disable16", 47), ("profile30Us0Disable1", 48), ("profile30Us0Disable2", 49), ("profile30Us0Disable3", 50), ("profile30Us0Disable4", 51), ("profile30Us0Disable5", 52), ("profile30Us0Disable6", 53), ("profile30Us0Disable7", 54), ("profile30Us0Disable8", 55), ("profile30Us0Disable9", 56), ("profile30Us0Disable10", 57), ("profile30Us0Disable11", 58), ("profile30Us0Disable12", 59), ("profile30Us0Disable13", 60), ("profile30Us0Disable14", 61), ("profile30Us0Disable15", 62), ("profile30Us0Disable16", 63))

class Xdsl2LineUs0Mask(TextualConvention, Bits):
    description = 'The US0 PSD masks to be allowed by the near-end xTU on the line. This parameter is only defined for G.993.2 Annex A. It is represented as a bitmap (0 if not allowed and 1 if allowed) with the following definitions.'
    status = 'current'
    namedValues = NamedValues(("eu32", 0), ("eu36", 1), ("eu40", 2), ("eu44", 3), ("eu48", 4), ("eu52", 5), ("eu56", 6), ("eu60", 7), ("eu64", 8), ("eu128", 9), ("reserved1", 10), ("reserved2", 11), ("reserved3", 12), ("reserved4", 13), ("reserved5", 14), ("reserved6", 15), ("adlu32", 16), ("adlu36", 17), ("adlu40", 18), ("adlu44", 19), ("adlu48", 20), ("adlu52", 21), ("adlu56", 22), ("adlu60", 23), ("adlu64", 24), ("adlu128", 25), ("reserved7", 26), ("reserved8", 27), ("reserved9", 28), ("reserved10", 29), ("reserved11", 30), ("reserved12", 31))

class Xdsl2SymbolProtection(TextualConvention, Integer32):
    description = "This type specifies the minimum impulse noise protection for the bearer channel if it is transported over DMT symbols with a subcarrier spacing of 4.3125 kHz. The possible values are: 'noProtection' (i.e., INP not required), 'halfSymbol' (i.e., INP length is 1/2 symbol), and 1-16 symbols in steps of 1 symbol."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18))
    namedValues = NamedValues(("noProtection", 1), ("halfSymbol", 2), ("singleSymbol", 3), ("twoSymbols", 4), ("threeSymbols", 5), ("fourSymbols", 6), ("fiveSymbols", 7), ("sixSymbols", 8), ("sevenSymbols", 9), ("eightSymbols", 10), ("nineSymbols", 11), ("tenSymbols", 12), ("elevenSymbols", 13), ("twelveSymbols", 14), ("thirteeSymbols", 15), ("fourteenSymbols", 16), ("fifteenSymbols", 17), ("sixteenSymbols", 18))

class Xdsl2SymbolProtection8(TextualConvention, Integer32):
    description = "This type specifies the minimum impulse noise protection for the bearer channel if it is transported over DMT symbols with a subcarrier spacing of 8.625 kHz. The possible values are: 'noProtection' (i.e., INP not required) and 1-16 symbols in steps of 1 symbol."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17))
    namedValues = NamedValues(("noProtection", 1), ("singleSymbol", 2), ("twoSymbols", 3), ("threeSymbols", 4), ("fourSymbols", 5), ("fiveSymbols", 6), ("sixSymbols", 7), ("sevenSymbols", 8), ("eightSymbols", 9), ("nineSymbols", 10), ("tenSymbols", 11), ("elevenSymbols", 12), ("twelveSymbols", 13), ("thirteeSymbols", 14), ("fourteenSymbols", 15), ("fifteenSymbols", 16), ("sixteenSymbols", 17))

class Xdsl2MaxBer(TextualConvention, Integer32):
    description = 'Objects with this syntax are configuration parameters that reference the maximum Bit Error Rate (BER). The possible values are: eminus3 (1) - Maximum BER=E^-3 eminus5 (2) - Maximum BER=E^-5 eminus7 (3) - Maximum BER=E^-7'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("eminus3", 1), ("eminus5", 2), ("eminus7", 3))

class Xdsl2ChInitPolicy(TextualConvention, Integer32):
    description = 'This syntax serves for channel configuration parameters that reference the channel initialization policy. The possible values are: policy0 (1) - Policy 0 according to the applicable standard. policy1 (2) - Policy 1 according to the applicable standard.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("policy0", 1), ("policy1", 2))

class Xdsl2ScMaskDs(TextualConvention, OctetString):
    description = 'Each one of the 4096 bits in this OCTET STRING array represents the corresponding subcarrier in the downstream direction. A bit value of one indicates that a subcarrier is masked.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 512)

class Xdsl2ScMaskUs(TextualConvention, OctetString):
    description = 'Each one of the 4096 bits in this OCTET STRING array represents the corresponding subcarrier in the upstream direction. A bit value of one indicates that a subcarrier is masked.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 512)

class Xdsl2CarMask(TextualConvention, OctetString):
    description = 'This type defines an array of bands. Each band is represented by 4 octets and there is a maximum of 32 bands allowed. Each band consists of a 16-bit start subcarrier index followed by a 16-bit stop subcarrier index. The subcarrier index is an unsigned number in the range 0 to NSC-1.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 128)

class Xdsl2RfiBands(TextualConvention, OctetString):
    description = 'This type defines a subset of downstream PSD mask breakpoints used to notch radio frequency interference (RFI) bands. Each RFI band is represented by 4 octets: a 16-bit start subcarrier index followed by a 16-bit stop subcarrier index. There is a maximum of 16 RFI bands allowed. The subcarrier index is an unsigned number in the range 0 to NSC-1.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 64)

class Xdsl2PsdMaskDs(TextualConvention, OctetString):
    description = 'This is a structure that represents up to 32 PSD mask breakpoints. Each breakpoint occupies 3 octets: The first two octets hold the index of the subcarrier associated with the breakpoint. The third octet holds the PSD reduction at the breakpoint from 0 (0 dBm/Hz) to 255 (-127.5 dBm/Hz) using units of 0.5 dBm/Hz. The subcarrier index is an unsigned number in the range 0 to NSCds-1.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 96)

class Xdsl2PsdMaskUs(TextualConvention, OctetString):
    description = 'This is a structure that represents up to 16 PSD mask breakpoints. Each breakpoint occupies 3 octets: The first two octets hold the index of the subcarrier associated with the breakpoint. The third octet holds the PSD reduction at the breakpoint from 0 (0 dBm/Hz) to 255 (-127.5 dBm/Hz) using units of 0.5 dBm/Hz. The subcarrier index is an unsigned number in the range 0 to NSCus-1.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 48)

class Xdsl2Tssi(TextualConvention, OctetString):
    description = 'This is a structure that represents up to 32 transmit spectrum shaping (TSSi) breakpoints. Each breakpoint is a pair of values occupying 3 octets with the following structure: First 2 octets - Index of the subcarrier used in the context of the breakpoint. Third octet - The shaping parameter at the breakpoint. The shaping parameter value is in the range 0 to 126 (units of -0.5 dB). The special value 127 indicates that the subcarrier is not transmitted. The subcarrier index is an unsigned number in the range 0 to NSC-1.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 96)

class Xdsl2LastTransmittedState(TextualConvention, Integer32):
    description = 'This parameter represents the last successful transmitted initialization state in the last full initialization performed on the line. States are per the specific xDSL technology and are numbered from 0 (if G.994.1 is used) or 1 (if G.994.1 is not used) up to Showtime.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318, 319, 320))
    namedValues = NamedValues(("atucG9941", 0), ("atucQuiet1", 1), ("atucComb1", 2), ("atucQuiet2", 3), ("atucComb2", 4), ("atucIcomb1", 5), ("atucLineprob", 6), ("atucQuiet3", 7), ("atucComb3", 8), ("atucIComb2", 9), ("atucMsgfmt", 10), ("atucMsgpcb", 11), ("atucQuiet4", 12), ("atucReverb1", 13), ("atucTref1", 14), ("atucReverb2", 15), ("atucEct", 16), ("atucReverb3", 17), ("atucTref2", 18), ("atucReverb4", 19), ("atucSegue1", 20), ("atucMsg1", 21), ("atucReverb5", 22), ("atucSegue2", 23), ("atucMedley", 24), ("atucExchmarker", 25), ("atucMsg2", 26), ("atucReverb6", 27), ("atucSegue3", 28), ("atucParams", 29), ("atucReverb7", 30), ("atucSegue4", 31), ("atucShowtime", 32), ("aturG9941", 100), ("aturQuiet1", 101), ("aturComb1", 102), ("aturQuiet2", 103), ("aturComb2", 104), ("aturIcomb1", 105), ("aturLineprob", 106), ("aturQuiet3", 107), ("aturComb3", 108), ("aturIcomb2", 109), ("aturMsgfmt", 110), ("aturMsgpcb", 111), ("aturReverb1", 112), ("aturQuiet4", 113), ("aturReverb2", 114), ("aturQuiet5", 115), ("aturReverb3", 116), ("aturEct", 117), ("aturReverb4", 118), ("aturSegue1", 119), ("aturReverb5", 120), ("aturSegue2", 121), ("aturMsg1", 122), ("aturMedley", 123), ("aturExchmarker", 124), ("aturMsg2", 125), ("aturReverb6", 126), ("aturSegue3", 127), ("aturParams", 128), ("aturReverb7", 129), ("aturSegue4", 130), ("aturShowtime", 131), ("vtucG9941", 200), ("vtucQuiet1", 201), ("vtucChDiscov1", 202), ("vtucSynchro1", 203), ("vtucPilot1", 204), ("vtucQuiet2", 205), ("vtucPeriodic1", 206), ("vtucSynchro2", 207), ("vtucChDiscov2", 208), ("vtucSynchro3", 209), ("vtucTraining1", 210), ("vtucSynchro4", 211), ("vtucPilot2", 212), ("vtucTeq", 213), ("vtucEct", 214), ("vtucPilot3", 215), ("vtucPeriodic2", 216), ("vtucTraining2", 217), ("vtucSynchro5", 218), ("vtucMedley", 219), ("vtucSynchro6", 220), ("vtucShowtime", 221), ("vturG9941", 300), ("vturQuiet1", 301), ("vturChDiscov1", 302), ("vturSynchro1", 303), ("vturLineprobe", 304), ("vturPeriodic1", 305), ("vturSynchro2", 306), ("vturChDiscov2", 307), ("vturSynchro3", 308), ("vturQuiet2", 309), ("vturTraining1", 310), ("vturSynchro4", 311), ("vturTeq", 312), ("vturQuiet3", 313), ("vturEct", 314), ("vturPeriodic2", 315), ("vturTraining2", 316), ("vturSynchro5", 317), ("vturMedley", 318), ("vturSynchro6", 319), ("vturShowtime", 320))

class Xdsl2LineStatus(TextualConvention, Bits):
    description = 'Objects with this syntax are status parameters that reflect the failure status for a given endpoint of a VDSL2/ADSL/ADSL2 or ADSL2+ link. This BITS structure can report the following failures: noDefect (0) - This bit position positively reports that no defect or failure exist. lossOfFraming (1) - Loss of frame synchronization. lossOfSignal (2) - Loss of signal. lossOfPower (3) - Loss of power. Usually this failure may be reported for CPE units only. initFailure (4) - Recent initialization process failed. Never active on xTU-R.'
    status = 'current'
    namedValues = NamedValues(("noDefect", 0), ("lossOfFraming", 1), ("lossOfSignal", 2), ("lossOfPower", 3), ("initFailure", 4))

class Xdsl2ChInpReport(TextualConvention, Integer32):
    description = "This type is used to indicate the method used to compute the Actual Impulse Noise Protection (ACTINP). If set to 'inpComputedUsingFormula', the ACTINP is computed according to the INP_no_erasure formula (9.6/G.993.2). If set to 'inpEstimatedByXtur', the ACTINP is the value estimated by the xTU receiver. inpComputedUsingFormula (1) - ACTINP computed using INP_no_erasure formula. inpEstimatedByXtur (2) - ACTINP estimated by the xTU receiver."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("inpComputedUsingFormula", 1), ("inpEstimatedByXtur", 2))

class Xdsl2ChAtmStatus(TextualConvention, Bits):
    description = 'Objects with this syntax are status parameters that reflect the failure status for the Transmission Convergence (TC) layer of a given ATM interface (data path over a VDSL2/ADSL/ ADSL2 or ADSL2+ link). This BITS structure can report the following failures: noDefect (0) - This bit position positively reports that no defect or failure exists. noCellDelineation (1) - The link was successfully initialized, but cell delineation was never acquired on the associated ATM data path. lossOfCellDelineation (2)- Loss of cell delineation on the associated ATM data path.'
    status = 'current'
    namedValues = NamedValues(("noDefect", 0), ("noCellDelineation", 1), ("lossOfCellDelineation", 2))

class Xdsl2ChPtmStatus(TextualConvention, Bits):
    description = 'Objects with this syntax are status parameters that reflect the failure status for a given PTM interface (packet data path over a VDSL2/ADSL/ADSL2 or ADSL2+ link). This BITS structure can report the following failures: noDefect (0) - This bit position positively reports that no defect or failure exists. outOfSync (1) - Out of synchronization.'
    status = 'current'
    namedValues = NamedValues(("noDefect", 0), ("outOfSync", 1))

class Xdsl2UpboKLF(TextualConvention, Integer32):
    description = 'Defines the upstream power backoff force mode (UPBOKLF). The three possible mode values are: auto(1) - The VDSL Transceiver Unit (VTUs) will autonomously determine the electrical length. override(2) - Forces the VTU-R to use the electrical length, kl0, of the CO-MIB (UPBOKL) to compute the UPBO. disableUpbo(3) - Disables UPBO such that UPBO is not utilized.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("auto", 1), ("override", 2), ("disableUpbo", 3))

class Xdsl2BandUs(TextualConvention, Integer32):
    description = 'Each value identifies a specific band in the upstream transmission direction (excluding the US0 band.). The possible values that identify a band are as follows: us1(5) - Upstream band number 1 (US1). us2(7) - Upstream band number 2 (US2). us3(9) - Upstream band number 3 (US3). us4(11) - Upstream band number 4 (US4).'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(5, 7, 9, 11))
    namedValues = NamedValues(("us1", 5), ("us2", 7), ("us3", 9), ("us4", 11))

class Xdsl2LinePsdMaskSelectUs(TextualConvention, Integer32):
    description = 'This type is used to define which upstream PSD mask is enabled. This type is used only for Annexes J and M of ITU-T Recommendations G.992.3 and G.992.5. adlu32Eu32 (1), - ADLU-32 / EU-32 adlu36Eu36 (2), - ADLU-36 / EU-36 adlu40Eu40 (3), - ADLU-40 / EU-40 adlu44Eu44 (4), - ADLU-44 / EU-44 adlu48Eu48 (5), - ADLU-48 / EU-48 adlu52Eu52 (6), - ADLU-52 / EU-52 adlu56Eu56 (7), - ADLU-56 / EU-56 adlu60Eu60 (8), - ADLU-60 / EU-60 adlu64Eu64 (9) - ADLU-64 / EU-64'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))
    namedValues = NamedValues(("adlu32Eu32", 1), ("adlu36Eu36", 2), ("adlu40Eu40", 3), ("adlu44Eu44", 4), ("adlu48Eu48", 5), ("adlu52Eu52", 6), ("adlu56Eu56", 7), ("adlu60Eu60", 8), ("adlu64Eu64", 9))

class Xdsl2LineCeFlag(TextualConvention, Bits):
    description = "This type is used to enable the use of the optional cyclic extension values. If the bit is set to '1', the optional cyclic extension values may be used. Otherwise, the cyclic extension shall be forced to the mandatory length (5N/32). enableCyclicExtension (0) - Enable use of optional Cyclic Extension values."
    status = 'current'
    namedValues = NamedValues(("enableCyclicExtension", 0))

class Xdsl2LineSnrMode(TextualConvention, Integer32):
    description = 'This type is used to enable the transmitter-referred virtual noise. The value of 1, indicates that virtual noise is disabled. The value of 2, indicates that virtual noise is enabled. virtualNoiseDisabled (1) - virtual noise is disabled. virtualNoiseEnabled (2) - virtual noise is enabled.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("virtualNoiseDisabled", 1), ("virtualNoiseEnabled", 2))

class Xdsl2LineTxRefVnDs(TextualConvention, OctetString):
    description = 'This is a structure that represents up to 32 PSD mask breakpoints. Each breakpoint occupies 3 octets: The first two octets hold the index of the subcarrier associated with the breakpoint. The third octet holds the PSD reduction at the breakpoint from 0 (-140 dBm/Hz) to 200 (-40 dBm/Hz) using units of 0.5 dBm/Hz. A special value of 255 indicates a noise level of 0 W/Hz. The subcarrier index is an unsigned number in the range 0 to NSCds-1.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 96)

class Xdsl2LineTxRefVnUs(TextualConvention, OctetString):
    description = 'This is a structure that represents up to 16 PSD mask breakpoints. Each breakpoint occupies 3 octets: The first two octets hold the index of the subcarrier associated with the breakpoint. The third octet holds the PSD reduction at the breakpoint from 0 (-140 dBm/Hz) to 200 (-40 dBm/Hz) using units of 0.5 dBm/Hz. A special value of 255 indicates a noise level of 0 W/Hz. The subcarrier index is an unsigned number in the range 0 to NSCus-1.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 48)

class Xdsl2BitsAlloc(TextualConvention, OctetString):
    description = 'This type specifies an array of nibbles, where each nibble indicates the bits allocation for a subcarrier. Each nibble has a value in the range 0 to 15 to indicate the bits allocation.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 256)

class Xdsl2MrefPsdDs(TextualConvention, OctetString):
    description = 'Objects with this syntax are MEDLEY Reference PSD status parameters in the downstream direction. This is expressed as the set of breakpoints exchanged at initialization. The OCTET STRING contains up to 48 pairs of values in the following structure: Octets 0-1 -- Index of the first subcarrier used in the context of a first breakpoint. Octets 2-3 -- The PSD level for the subcarrier indicated in octets 0-1. Octets 4-7 -- Same, for a second breakpoint Octets 8-11 -- Same, for a third breakpoint And so on until Octets 188-191 -- Same, for a 48th breakpoint. The subcarrier index is an unsigned number in the range 0 to NSCds-1. The PSD level is an integer value in the 0 to 4095 range. It is represented in units of 0.1 dB offset from -140 dBm/Hz.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 192)

class Xdsl2MrefPsdUs(TextualConvention, OctetString):
    description = 'Objects with this syntax are MEDLEY Reference PSD status parameters in the upstream direction. This is expressed as the set of breakpoints exchanged at initialization. The OCTET STRING contains up to 32 pairs of values in the following structure: Octets 0-1 -- Index of the first subcarrier used in the context of a first breakpoint. Octets 2-3 -- The PSD level for the subcarrier indicated in octets 0-1. Octets 4-7 -- Same, for a second breakpoint Octets 8-11 -- Same, for a third breakpoint And so on until Octets 124-127 -- Same, for a 32nd breakpoint. The subcarrier index is an unsigned number in the range 0 to NSCus-1. The PSD level is an integer value in the 0 to 4095 range. It is represented in units of 0.1 dB offset from -140 dBm/Hz.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 128)

mibBuilder.exportSymbols("VDSL2-LINE-TC-MIB", Xdsl2ScMaskUs=Xdsl2ScMaskUs, vdsl2TCMIB=vdsl2TCMIB, Xdsl2Unit=Xdsl2Unit, Xdsl2SymbolProtection8=Xdsl2SymbolProtection8, Xdsl2LdsfResult=Xdsl2LdsfResult, Xdsl2SymbolProtection=Xdsl2SymbolProtection, Xdsl2BitsAlloc=Xdsl2BitsAlloc, Xdsl2MrefPsdUs=Xdsl2MrefPsdUs, Xdsl2PowerMngState=Xdsl2PowerMngState, Xdsl2OperationModes=Xdsl2OperationModes, Xdsl2CarMask=Xdsl2CarMask, Xdsl2InitResult=Xdsl2InitResult, Xdsl2LineReset=Xdsl2LineReset, Xdsl2PsdMaskDs=Xdsl2PsdMaskDs, PYSNMP_MODULE_ID=vdsl2TCMIB, Xdsl2PsdMaskUs=Xdsl2PsdMaskUs, Xdsl2LinePmMode=Xdsl2LinePmMode, Xdsl2LinePsdMaskSelectUs=Xdsl2LinePsdMaskSelectUs, Xdsl2LineSnrMode=Xdsl2LineSnrMode, Xdsl2ChAtmStatus=Xdsl2ChAtmStatus, Xdsl2RfiBands=Xdsl2RfiBands, Xdsl2LineLdsf=Xdsl2LineLdsf, Xdsl2ScMaskDs=Xdsl2ScMaskDs, Xdsl2LineTxRefVnUs=Xdsl2LineTxRefVnUs, Xdsl2RaMode=Xdsl2RaMode, Xdsl2MrefPsdDs=Xdsl2MrefPsdDs, Xdsl2Tssi=Xdsl2Tssi, Xdsl2BpscResult=Xdsl2BpscResult, Xdsl2LineStatus=Xdsl2LineStatus, Xdsl2Direction=Xdsl2Direction, Xdsl2LineClassMask=Xdsl2LineClassMask, Xdsl2ChInpReport=Xdsl2ChInpReport, Xdsl2LineBpsc=Xdsl2LineBpsc, Xdsl2BandUs=Xdsl2BandUs, Xdsl2LineUs0Mask=Xdsl2LineUs0Mask, Xdsl2TransmissionModeType=Xdsl2TransmissionModeType, Xdsl2LineUs0Disable=Xdsl2LineUs0Disable, Xdsl2Band=Xdsl2Band, Xdsl2LastTransmittedState=Xdsl2LastTransmittedState, Xdsl2ChInitPolicy=Xdsl2ChInitPolicy, Xdsl2UpboKLF=Xdsl2UpboKLF, Xdsl2LineLimitMask=Xdsl2LineLimitMask, Xdsl2LineCeFlag=Xdsl2LineCeFlag, Xdsl2ChPtmStatus=Xdsl2ChPtmStatus, Xdsl2LineTxRefVnDs=Xdsl2LineTxRefVnDs, Xdsl2LineProfiles=Xdsl2LineProfiles, Xdsl2MaxBer=Xdsl2MaxBer, Xdsl2ConfPmsForce=Xdsl2ConfPmsForce)
