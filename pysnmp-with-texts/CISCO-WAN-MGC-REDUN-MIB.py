#
# PySNMP MIB module CISCO-WAN-MGC-REDUN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-WAN-MGC-REDUN-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:18:45 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
mgProtocolNumber, mgcNumber = mibBuilder.importSymbols("CISCO-WAN-MG-MIB", "mgProtocolNumber", "mgcNumber")
ciscoWan, = mibBuilder.importSymbols("CISCOWAN-SMI", "ciscoWan")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, Counter64, Counter32, IpAddress, Unsigned32, MibIdentifier, NotificationType, Integer32, TimeTicks, Bits, iso, ModuleIdentity, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "Counter64", "Counter32", "IpAddress", "Unsigned32", "MibIdentifier", "NotificationType", "Integer32", "TimeTicks", "Bits", "iso", "ModuleIdentity", "ObjectIdentity")
TextualConvention, TruthValue, RowStatus, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TruthValue", "RowStatus", "DisplayString")
ciscoWanMgcRedunMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 351, 150, 22))
ciscoWanMgcRedunMIB.setRevisions(('2004-01-19 00:00', '2001-12-26 00:00', '2001-07-19 15:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoWanMgcRedunMIB.setRevisionsDescriptions(('Update MIB with description changes', 'Added mgcRedundancyGrpProtocolRowStatus, mgcRedGrpProtPersistEvtPolicy, mgcRedGrpProtQuarantinePolicy, mgcRedGrpProtSigEvtOnOffPolicy, mgcRedGrpProtProvisionalResponse, mgcRedGrpProtResponseAckAttr, mgcRedGrpProtDisconnectProcedure, mgcRedGrpProtCancelGraceful for MGCP1.0 enhancements.', 'Initial version of the MIB',))
if mibBuilder.loadTexts: ciscoWanMgcRedunMIB.setLastUpdated('200401190000Z')
if mibBuilder.loadTexts: ciscoWanMgcRedunMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoWanMgcRedunMIB.setContactInfo(' Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-vism@cisco.com')
if mibBuilder.loadTexts: ciscoWanMgcRedunMIB.setDescription('The MIB module for Media Gateways (MGs) to allow multiple Media Gateway Controllers (MGCs) to be configured and managed on the Gateway. MGCs can be group together as part of the same MGC redundancy group. Terms used: CA: Call Agent GW: Gateway MGC: Media Gateway Controller MGCP: Media Gateway Control Protocol NTFY: Notify message (MGCP standard message) RSIP: Restart In Progress (MGCP standard message) RSVP: Resource Reservation Setup Protocol SGCP: Simple Gateway Control Protocol SRCP: Simple Resource Coordination Protocol')
mgcRedundancyObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 22, 1))
mgcRedundancyGrpTable = MibTable((1, 3, 6, 1, 4, 1, 351, 150, 22, 1, 1), )
if mibBuilder.loadTexts: mgcRedundancyGrpTable.setStatus('current')
if mibBuilder.loadTexts: mgcRedundancyGrpTable.setDescription('Multiple Media Gateway Controllers can be grouped together as part of the same MGC redundancy group. This configuration supports the notion of redundant Media Gateway Controllers. This table keeps track of the MGCs in a redundancy group. It is used to create MGC redundancy groups. MGCs can also be removed from a group.')
mgcRedundancyGrpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 351, 150, 22, 1, 1, 1), ).setIndexNames((0, "CISCO-WAN-MGC-REDUN-MIB", "mgcRedundancyGrpNum"), (0, "CISCO-WAN-MG-MIB", "mgcNumber"))
if mibBuilder.loadTexts: mgcRedundancyGrpEntry.setStatus('current')
if mibBuilder.loadTexts: mgcRedundancyGrpEntry.setDescription('Each row in the table is identified by an mgcRedundancyGrpNum and mgcNumber. Before adding an entry into this table the MGC has to be added in mgcTable defined in CISCO-WAN-MG-MIB. A single mgcRedundancyGrp can have multiple MGCs.')
mgcRedundancyGrpNum = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 22, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)))
if mibBuilder.loadTexts: mgcRedundancyGrpNum.setStatus('current')
if mibBuilder.loadTexts: mgcRedundancyGrpNum.setDescription('This is the MGC group number. A group can contain more than 1 MGC. So for a group containing more than 1 MGC, there will be more than 1 row of this table that will have a common group number.')
mgcRedundancyGrpPref = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 22, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mgcRedundancyGrpPref.setStatus('current')
if mibBuilder.loadTexts: mgcRedundancyGrpPref.setDescription("Allows to configure the preference on a MGCs. The GW use this object in the selection of an MGC when there are multiple MGCs in the same MGC redundancy group. This object can be modified at any time while the mgcRedundancyGrpRowStatus is 'active'. It has to be unique among various MGCs of a same MGC redundancy group. The lower the number the higher the preference, for example 1 will have higher preference than 2.")
mgcRedundancyGrpActState = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 22, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("mgcActive", 1), ("mgcInactive", 2))).clone('mgcInactive')).setMaxAccess("readonly")
if mibBuilder.loadTexts: mgcRedundancyGrpActState.setStatus('current')
if mibBuilder.loadTexts: mgcRedundancyGrpActState.setDescription("This object is used to denote the status of MGC within an MGC Redundancy group. 'mgcActive' - Indicates the MGC is active or controlling the GW. 'mgcInactive' - Indicates the MGC is in standby state.")
mgcRedundancyGrpRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 22, 1, 1, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mgcRedundancyGrpRowStatus.setStatus('current')
if mibBuilder.loadTexts: mgcRedundancyGrpRowStatus.setDescription("Controls the creation and deletion of a table entry. An entry may be created using the 'createAndGo' option. When the row is successfully created, the RowStatus would be set to 'active' by the agent. An entry may be deleted by setting the RowStatus to 'destroy'. Other options such as `createAndWait', 'notInService', 'notReady' are not supported. mgcRedundancyGrpNum, mgcNumber and mgcRedundancyGrpPref are the mandatory parameters while creating an entry.")
mgcRedundancyGrpParamTable = MibTable((1, 3, 6, 1, 4, 1, 351, 150, 22, 1, 2), )
if mibBuilder.loadTexts: mgcRedundancyGrpParamTable.setStatus('current')
if mibBuilder.loadTexts: mgcRedundancyGrpParamTable.setDescription('This table contains the parameters of the MGC redundancy groups like the association state and priority of the group within the GW. An entry in this table is implicitly created when the first MGC is added for an MGC redundancy group. The objects are set to their default values. When the last MGC from an MGC redundancy group is removed, the corresponding entry from this table is implicitly removed.')
mgcRedundancyGrpParamEntry = MibTableRow((1, 3, 6, 1, 4, 1, 351, 150, 22, 1, 2, 1), ).setIndexNames((0, "CISCO-WAN-MGC-REDUN-MIB", "mgcRedundancyGrpNum"))
if mibBuilder.loadTexts: mgcRedundancyGrpParamEntry.setStatus('current')
if mibBuilder.loadTexts: mgcRedundancyGrpParamEntry.setDescription('Represents an individual entry in the mgcRedundancyGrpParamTable.')
mgcRedundancyGrpStateChangeNtfy = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 22, 1, 2, 1, 1), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mgcRedundancyGrpStateChangeNtfy.setStatus('current')
if mibBuilder.loadTexts: mgcRedundancyGrpStateChangeNtfy.setDescription("This object 'true(1) will enable sending state change notifications to the MGC. 'false(2)' will disable sending state change notifications to MGC, for example, if MGCP/SGCP is the protocol used, then RSIPs are sent to the MGC if this object is set to 'true(1)'.")
mgcRedundancyGrpCommState = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 22, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("commOk", 1), ("commLoss", 2))).clone('commLoss')).setMaxAccess("readonly")
if mibBuilder.loadTexts: mgcRedundancyGrpCommState.setStatus('current')
if mibBuilder.loadTexts: mgcRedundancyGrpCommState.setDescription("Represents the state of the communication between the GW and the MGC (call agent) group. The possible values are: 'commOk': This indicates that the communication between the gateway and the media gateway controller is ok. 'commLoss': This indicates that the communication between the GW and the MGC is lost. This object is set to 'commLoss' if no response is receive from any MGC in this group to a GW initiated message. If the GW is able to successfully send a message to the MGC or if a message is received from the MGC, the value of this object is set to 'commOk' else it will remain in the 'commLoss' state.")
mgcRedundancyGrpPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 22, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mgcRedundancyGrpPriority.setStatus('current')
if mibBuilder.loadTexts: mgcRedundancyGrpPriority.setDescription('This field determines the priority amongst the MGC redundancy groups within the GW. A MGC group with a priority of 0 means that the MGC group is not interested in receiving GW initiated messages. A group with a priority value of 1 has the highest preference. A higher value indicates a lower preference. Multiple MGC redundancy groups can have the same priority.')
mgcRedundancyGrpProtocolTable = MibTable((1, 3, 6, 1, 4, 1, 351, 150, 22, 1, 3), )
if mibBuilder.loadTexts: mgcRedundancyGrpProtocolTable.setStatus('current')
if mibBuilder.loadTexts: mgcRedundancyGrpProtocolTable.setDescription('This table contains information about which protocols are being used in a particular association between the gateway and the MGC redundancy groups. Because there may be a number of different protocols in use for a particular control association between the gateway and an MGC group, this information is kept in a separate table rather than being included in mgcRedundancyGrpTable. In effect, it constitutes a relationship between mgcRedundancyGrpTable and mgSupportedProtocolTable defined in CISCO-WAN-MG-MIB. This table restricts all MGCs within a MGC redundancy group to have the same set of protocols defined.')
mgcRedundancyGrpProtocolEntry = MibTableRow((1, 3, 6, 1, 4, 1, 351, 150, 22, 1, 3, 1), ).setIndexNames((0, "CISCO-WAN-MGC-REDUN-MIB", "mgcRedundancyGrpNum"), (0, "CISCO-WAN-MG-MIB", "mgProtocolNumber"))
if mibBuilder.loadTexts: mgcRedundancyGrpProtocolEntry.setStatus('current')
if mibBuilder.loadTexts: mgcRedundancyGrpProtocolEntry.setDescription('Represents an individual table entry in mgcRedundancyGrpProtocolTable. When active, it is expected that mgcRedundancyGrpNum and mgProtocolNumber contain valid values that maintain referential integrity into mgcRedundancyGrpTable and mgSupportedProtocolTable respectively. The attempt to create a row that would violate referential integrity shall be rejected.')
mgcRedundancyGrpProtocolRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 22, 1, 3, 1, 1), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mgcRedundancyGrpProtocolRowStatus.setStatus('current')
if mibBuilder.loadTexts: mgcRedundancyGrpProtocolRowStatus.setDescription("Controls the creation and deletion of a table entry. An entry may be created using the 'createAndGo' option. When the row is successfully created, the mgcRedundancyGrpProtocolRowStatus would be set to 'active' by the agent. An entry can be modified at any time while the mgcRedundancyGrpProtocolRowStatus is 'active'. An entry may be deleted by setting the mgcRedundancyGrpProtocolRowStatus to 'destroy'.")
mgcRedGrpProtPersistEvtPolicy = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 22, 1, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("quarantinePersistEvts", 1), ("notQuarantinePersistEvts", 2))).clone('quarantinePersistEvts')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mgcRedGrpProtPersistEvtPolicy.setStatus('current')
if mibBuilder.loadTexts: mgcRedGrpProtPersistEvtPolicy.setDescription("This object determines how the persistent events will be notified. Persistent events are events that call agent wants to be notified without explicitly requesting for it. A set of events can be provisioned on the Gateway as persistent events. Every event will have an action associated with it, which will determine, whether to be notified, ignored, accumulated etc.. MGC will specify the action when requesting the GW to notify the event. For persistent events the Action will be Notify. Call agent can change this by explicitly requesting the event associating an action with it. During the period where the Gateway has received a notification acknowledgement, and waiting for the next Request Notification, events could be observed. The Quarantine procedure determines what should be done with these events. This object is used to supercede the quarantine procedure, by enforcing loop, process as the quarantine procedure only for persistent events. During the period the Gateway has sent a Notification, and waiting for the acknowledgement all events including the persistent events will 'quarantinePersistEvts' - Quarantine Persistent events as in the case of non persistent events as determined by quarantine method. 'notQuarantinePersistEvts' - Don't quarantine Persistent events, and notify them. During the period the Gateway has sent a Notify and waiting for the acknowledgement, every event including persistent event will be quarantined. This value does not supercede that behaviour. This applies only during the period, where a Notify is acknowledged and waiting for the next RQNT where the quarantine method is 'step,process' or 'step,discard'. This object has no relevance when the protocol is SRCP.")
mgcRedGrpProtQuarantinePolicy = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 22, 1, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("stepProcess", 1), ("stepDiscard", 2), ("loopProcess", 3), ("loopDiscard", 4)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mgcRedGrpProtQuarantinePolicy.setReference('Media Gateway Control Protocol (MGCP), version 1.0 bis, May 10, 2001 : Sections 3.2.2.18, 3.3.1, 3.3.2.')
if mibBuilder.loadTexts: mgcRedGrpProtQuarantinePolicy.setStatus('current')
if mibBuilder.loadTexts: mgcRedGrpProtQuarantinePolicy.setDescription("This object determines the quarantine policy when MGC doesn't explicitly specify one. When a Request Notification is received from the MGC, the Gateway on observing the first event that qualifies to be notified will generate a Notify message with the list of observed events including the event which triggered the Notify. After the MGC acknowledges the Notify, if further events are observed and an event which qualifies to be notified, the Gateway may notify the event, or quarantine it until the next Request Notification, based on the quarantine policy set by the MGC. When the MGC doesn't explicitly specify the quarantine policy, the protocol defines the default behaviour. The default behaviour varies with different versions of the protocol. This object allows the user to configure the default quarantine policy per protocol per redundancy group. The default value for this object will be set based on the protocol. 'stepProcess' - Process the events in the quarantine list, and after one Notify quarantine events until next Request Notification 'stepDiscard' - Discard the events in the quarantine list, and after one Notify quarantine events until next Request Notification 'loopProcess' - Process the events in the quarantine list, and notify observed events as and when need arises 'loopDiscard' - Discard the events in the quarantine list, and notify observed events as and when need arises The default value for MGCP 1.0 will be stepProcess and stepDiscard for the rest. This object has no relevance when the protocol is SRCP.")
mgcRedGrpProtSigEvtOnOffPolicy = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 22, 1, 3, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("deleteEventNotPresent", 1), ("deleteOnlyNegatedEvent", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mgcRedGrpProtSigEvtOnOffPolicy.setStatus('current')
if mibBuilder.loadTexts: mgcRedGrpProtSigEvtOnOffPolicy.setDescription("This object enables the user to provision the way signaled events from CA are handled by the gateway. This is configurable on a per MGC redundancy group, per protocol basis. If the protocol is MGCP 1.0 the default of this object is 'deleteOnlyNegatedEvent', else it is set to 'deleteEventNotPresent'. If this object is set to 'deleteOnlyNegatedEvent', then the signal currently active on a endpoint/connection can be turned OFF only by parameterizing it with a (-) for eg: S: T/co1(-) will turn off co1 event on an endpoint. And can be turned ON by just providing the signal name or by parameterizing the signal name with a (+) for eg: S:T/co1(+), L/hd will turn on co1 and hd events on the endpoint. If this object is set to 'deleteEventNotPresent', then the signal/s can be turned OFF by providing empty S: list. The signal can be turned ON by simply providing the signal name. for eg: S: will turn OFF all active signals on the endpoint S: T/co1 will turn ON co1 signal. The configuration of this object only applies to on/off signals and not for brief or timeout signals. MGCP 0.1 specification says if an empty signaled list is provided it is meant to turn off all the currently turned on signaled events. However in MGCP 1.0 specification, it says that unless specifically requested by the CA to turn off (signal is parameterized by a (-)) the signal cannot be turned off, in other words an empty signal list does imply that the currently active signals should be turned off. Although the behavior of the gateway is specified in the specs, some MGC may not follow the MGCP 1.0 spec. Hence this MIB serves as an interop knob. This object has no relevance when the protocol is SRCP.")
mgcRedGrpProtProvisionalResponse = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 22, 1, 3, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("sendProvisionalResponse", 1), ("notSendProvisionalResponse", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mgcRedGrpProtProvisionalResponse.setStatus('current')
if mibBuilder.loadTexts: mgcRedGrpProtProvisionalResponse.setDescription("This object enables or disables sending provisional response to the CA when processing a request received from the CA. The provisional response to the CA indicates that the GW is processing the request and will send a final response once the processing is complete. For example, if a CRCX request from the CA using MGCP protocol, requires that resources be reserved along the bearer path using RSVP, GW would send a provisional response if this parameter was set to true. It would then wait for the RSVP procedure to complete before sending the final response. On the other hand, if the value of this parameter was set to false, the final response will be sent out without waiting for the RSVP procedure to complete. When the RSVP procedure does complete, a NTFY will be sent from the GW indicating if the RSVP procedure was successful or not. The GW will receive provisional responses from the CA. These messages will be parsed and ignored regardless of this object. If the protocol supported by the CA is MGCP1.0, the default value for this object is 'sendProvisionalResponse'. In all other cases, it is 'notSendProvisionalResponse'. This object has no relevance when the protocol is SRCP.")
mgcRedGrpProtResponseAckAttr = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 22, 1, 3, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("sendResponseAckAttr", 1), ("notSendResponseAckAttr", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mgcRedGrpProtResponseAckAttr.setReference('Media Gateway Control Protocol (MGCP), version 1.0 bis, May 10, 2001 : Sections 3.2.2.18, 3.3.1, 3.3.2.')
if mibBuilder.loadTexts: mgcRedGrpProtResponseAckAttr.setStatus('current')
if mibBuilder.loadTexts: mgcRedGrpProtResponseAckAttr.setDescription("Every command from the MGC could contain Response Acknowledgement attribute. This attribute consists a list of transaction IDs which are acknowledged by the Call agent. The gateway on receiving this can free up the resources attached to this transaction ID. When this attribute is present in the Gateway response, it should contain an empty list of transaction ID. This attribute in the response from the Gateway is to invite a response acknowledgement message from the MGC for this response. This will be present in the final response sent by the gateway only when a provisional response had been sent prior to this final response for the same transaction. This object determines whether the Gateway should include response acknowledgement in the final response. This object does not determine the capability of the Gateway to receive response acknowledgement attribute as part of MGC commands. 'sendResponseAckAttr' - Gateway will include response acknowledgement attribute as part of final response when a provisional response had been sent earlier. 'notSendResponseAckAttr' - Gateway will not include response acknowledgement attribute as part of final response when a provisional response had been sent earlier. The default value will be 'sendResponseAckAttr' for MGCP 1.0 protocol and 'notSendResponseAckAttr' for every other protocol. This object has no relevance when the protocol is SRCP.")
mgcRedGrpProtDisconnectProcedure = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 22, 1, 3, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("doDisconnectProcedure", 1), ("notDoDisconnectProcedure", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mgcRedGrpProtDisconnectProcedure.setReference('Media Gateway Control Protocol (MGCP), version 1.0 bis, May 10, 2001 : Section 4.4.7.')
if mibBuilder.loadTexts: mgcRedGrpProtDisconnectProcedure.setStatus('current')
if mibBuilder.loadTexts: mgcRedGrpProtDisconnectProcedure.setDescription("This attribute describes whether disconnected procedure is enabled/disabled per protocol per MGC group configured. The endpoint becomes disconnected when a gateway initiated commands are sent to the MGC and has not received any response from the MGC. The disconnected endpoint initiates the disconnected procedure by sending Restart in Progress command with restart method RM:disconnected to the MGC. When the object is set to 'doDisconnectProcedure', then the endpoint will start the disconnected procedure and sends 'Restart In Progress' command with the restart method RM:disconnected to the MGC. By default, the object is set to 'doDisconnectProcedure' for MGCP 1.0 and 'notDoDisconnectProcedure' for all other protocols. This object has no relevance when the protocol is SRCP.")
mgcRedGrpProtCancelGraceful = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 22, 1, 3, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("sendCancelGraceful", 1), ("notSendCancelGraceful", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mgcRedGrpProtCancelGraceful.setReference('Media Gateway Control Protocol (MGCP), version 1.0 bis, May 10, 2001 : Section 4.4.7.')
if mibBuilder.loadTexts: mgcRedGrpProtCancelGraceful.setStatus('current')
if mibBuilder.loadTexts: mgcRedGrpProtCancelGraceful.setDescription("This attribute describes whether notification of RSIP cancel graceful is enabled/disabled per protocol per MGC group configured. The Restart in Progress command with the restart method of cancel graceful indicates that the gateway is canceling a previously issued 'graceful' restart in progress command. The endpoints are still in service. When the object is set to 'sendCancelGraceful', the gateway will send the Restart in Progress command with the restart method of cancel graceful indicating that it is canceling the previously sent 'graceful' Restart in Progress command. By default, the object is set to 'sendCancelGraceful' for MGCP 1.0 and 'notSendCancelGraceful' for all other protocols. This object has no relevance when the protocol is SRCP.")
mgcRedunNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 22, 2))
mgcRedunNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 22, 2, 0))
mgcRedunMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 22, 3))
mgcRedunMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 22, 3, 1))
mgcRedunMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 22, 3, 2))
mgcRedunMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 351, 150, 22, 3, 1, 1)).setObjects(("CISCO-WAN-MGC-REDUN-MIB", "mgcRedundancyGroup"), ("CISCO-WAN-MGC-REDUN-MIB", "mgcRedundancyParamGroup"), ("CISCO-WAN-MGC-REDUN-MIB", "mgcRedundancyProtocolGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mgcRedunMIBCompliance = mgcRedunMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: mgcRedunMIBCompliance.setDescription('The compliance statement for the SNMP entities which implement MGC-REDUN-MIB.')
mgcRedundancyGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 351, 150, 22, 3, 2, 1)).setObjects(("CISCO-WAN-MGC-REDUN-MIB", "mgcRedundancyGrpPref"), ("CISCO-WAN-MGC-REDUN-MIB", "mgcRedundancyGrpActState"), ("CISCO-WAN-MGC-REDUN-MIB", "mgcRedundancyGrpRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mgcRedundancyGroup = mgcRedundancyGroup.setStatus('current')
if mibBuilder.loadTexts: mgcRedundancyGroup.setDescription('This group contains objects that apply to the redundant media gateway controller group.')
mgcRedundancyParamGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 351, 150, 22, 3, 2, 2)).setObjects(("CISCO-WAN-MGC-REDUN-MIB", "mgcRedundancyGrpStateChangeNtfy"), ("CISCO-WAN-MGC-REDUN-MIB", "mgcRedundancyGrpCommState"), ("CISCO-WAN-MGC-REDUN-MIB", "mgcRedundancyGrpPriority"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mgcRedundancyParamGroup = mgcRedundancyParamGroup.setStatus('current')
if mibBuilder.loadTexts: mgcRedundancyParamGroup.setDescription('This group contains objects that describe the parameters of an MGC redundancy group.')
mgcRedundancyProtocolGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 351, 150, 22, 3, 2, 3)).setObjects(("CISCO-WAN-MGC-REDUN-MIB", "mgcRedundancyGrpProtocolRowStatus"), ("CISCO-WAN-MGC-REDUN-MIB", "mgcRedGrpProtPersistEvtPolicy"), ("CISCO-WAN-MGC-REDUN-MIB", "mgcRedGrpProtQuarantinePolicy"), ("CISCO-WAN-MGC-REDUN-MIB", "mgcRedGrpProtSigEvtOnOffPolicy"), ("CISCO-WAN-MGC-REDUN-MIB", "mgcRedGrpProtProvisionalResponse"), ("CISCO-WAN-MGC-REDUN-MIB", "mgcRedGrpProtResponseAckAttr"), ("CISCO-WAN-MGC-REDUN-MIB", "mgcRedGrpProtDisconnectProcedure"), ("CISCO-WAN-MGC-REDUN-MIB", "mgcRedGrpProtCancelGraceful"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mgcRedundancyProtocolGroup = mgcRedundancyProtocolGroup.setStatus('current')
if mibBuilder.loadTexts: mgcRedundancyProtocolGroup.setDescription('This group contains the protocols configured for an MGC redundancy group.')
mibBuilder.exportSymbols("CISCO-WAN-MGC-REDUN-MIB", mgcRedundancyProtocolGroup=mgcRedundancyProtocolGroup, mgcRedundancyGrpRowStatus=mgcRedundancyGrpRowStatus, mgcRedundancyGrpProtocolRowStatus=mgcRedundancyGrpProtocolRowStatus, PYSNMP_MODULE_ID=ciscoWanMgcRedunMIB, mgcRedundancyGrpEntry=mgcRedundancyGrpEntry, mgcRedundancyGrpProtocolTable=mgcRedundancyGrpProtocolTable, mgcRedunMIBGroups=mgcRedunMIBGroups, mgcRedundancyObjects=mgcRedundancyObjects, mgcRedundancyGrpActState=mgcRedundancyGrpActState, mgcRedundancyGrpPref=mgcRedundancyGrpPref, mgcRedundancyGrpTable=mgcRedundancyGrpTable, mgcRedunMIBConformance=mgcRedunMIBConformance, mgcRedGrpProtQuarantinePolicy=mgcRedGrpProtQuarantinePolicy, mgcRedundancyGrpParamTable=mgcRedundancyGrpParamTable, mgcRedGrpProtPersistEvtPolicy=mgcRedGrpProtPersistEvtPolicy, mgcRedunMIBCompliance=mgcRedunMIBCompliance, mgcRedGrpProtResponseAckAttr=mgcRedGrpProtResponseAckAttr, mgcRedundancyGrpNum=mgcRedundancyGrpNum, mgcRedunMIBCompliances=mgcRedunMIBCompliances, mgcRedunNotificationPrefix=mgcRedunNotificationPrefix, ciscoWanMgcRedunMIB=ciscoWanMgcRedunMIB, mgcRedundancyGrpProtocolEntry=mgcRedundancyGrpProtocolEntry, mgcRedundancyGrpStateChangeNtfy=mgcRedundancyGrpStateChangeNtfy, mgcRedGrpProtProvisionalResponse=mgcRedGrpProtProvisionalResponse, mgcRedGrpProtCancelGraceful=mgcRedGrpProtCancelGraceful, mgcRedundancyGrpCommState=mgcRedundancyGrpCommState, mgcRedGrpProtSigEvtOnOffPolicy=mgcRedGrpProtSigEvtOnOffPolicy, mgcRedundancyGroup=mgcRedundancyGroup, mgcRedundancyParamGroup=mgcRedundancyParamGroup, mgcRedundancyGrpParamEntry=mgcRedundancyGrpParamEntry, mgcRedunNotifications=mgcRedunNotifications, mgcRedundancyGrpPriority=mgcRedundancyGrpPriority, mgcRedGrpProtDisconnectProcedure=mgcRedGrpProtDisconnectProcedure)
