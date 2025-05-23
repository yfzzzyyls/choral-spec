# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: inference.proto
# Protobuf Python Version: 5.27.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    2,
    '',
    'inference.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0finference.proto\x12\nspecdecode\"Y\n\x0cStartRequest\x12\x12\n\nsession_id\x18\x01 \x01(\x04\x12\x0e\n\x06prompt\x18\x02 \x01(\t\x12\x16\n\x0emax_new_tokens\x18\x03 \x01(\r\x12\r\n\x05gamma\x18\x04 \x01(\r\"%\n\rStartResponse\x12\x14\n\x0c\x61\x63knowledged\x18\x01 \x01(\x08\"N\n\rDraftSequence\x12\x12\n\nsession_id\x18\x01 \x01(\x04\x12\x14\n\x0c\x64raft_tokens\x18\x02 \x03(\x05\x12\x13\n\x0b\x64raft_probs\x18\x03 \x03(\x02\"B\n\x12VerifyBatchRequest\x12,\n\tsequences\x18\x01 \x03(\x0b\x32\x19.specdecode.DraftSequence\"N\n\rVerifyRequest\x12\x12\n\nsession_id\x18\x01 \x01(\x04\x12\x14\n\x0c\x64raft_tokens\x18\x02 \x03(\x05\x12\x13\n\x0b\x64raft_probs\x18\x03 \x03(\x02\"c\n\x0cVerifyResult\x12\x12\n\nsession_id\x18\x01 \x01(\x04\x12\x17\n\x0ftokens_accepted\x18\x02 \x01(\r\x12\x14\n\x0ctarget_token\x18\x03 \x01(\x05\x12\x10\n\x08\x66inished\x18\x04 \x01(\x08\"@\n\x13VerifyBatchResponse\x12)\n\x07results\x18\x01 \x03(\x0b\x32\x18.specdecode.VerifyResult\"6\n\x10\x46inalizeSequence\x12\x12\n\nsession_id\x18\x01 \x01(\x04\x12\x0e\n\x06tokens\x18\x02 \x03(\x05\"G\n\x14\x46inalizeBatchRequest\x12/\n\tsequences\x18\x01 \x03(\x0b\x32\x1c.specdecode.FinalizeSequence\";\n\x13\x46inalizeBatchResult\x12\x12\n\nsession_id\x18\x01 \x01(\x04\x12\x10\n\x08\x66inished\x18\x02 \x01(\x08\"I\n\x15\x46inalizeBatchResponse\x12\x30\n\x07results\x18\x01 \x03(\x0b\x32\x1f.specdecode.FinalizeBatchResult\"Q\n\x0eVerifyResponse\x12\x15\n\rcommitted_ids\x18\x01 \x03(\x05\x12\x16\n\x0e\x61\x63\x63\x65pted_count\x18\x02 \x01(\r\x12\x10\n\x08\x66inished\x18\x03 \x01(\x08\"W\n\x0f\x46inalizeRequest\x12\x12\n\nsession_id\x18\x01 \x01(\x04\x12\x16\n\x0e\x61\x63\x63\x65pted_count\x18\x02 \x01(\r\x12\x18\n\x10\x64raft_chunk_size\x18\x03 \x01(\r\"9\n\x10\x46inalizeResponse\x12\x13\n\x0b\x66inal_token\x18\x01 \x01(\x05\x12\x10\n\x08\x66inished\x18\x02 \x01(\x08\"\x11\n\x0fGenerateRequest\"\'\n\x10GenerateResponse\x12\x13\n\x0boutput_text\x18\x01 \x01(\t2\xef\x03\n\x12SpeculativeService\x12\x46\n\x0fStartGeneration\x12\x18.specdecode.StartRequest\x1a\x19.specdecode.StartResponse\x12T\n\x11VerifyBatchTokens\x12\x1e.specdecode.VerifyBatchRequest\x1a\x1f.specdecode.VerifyBatchResponse\x12Z\n\x13\x46inalizeBatchTokens\x12 .specdecode.FinalizeBatchRequest\x1a!.specdecode.FinalizeBatchResponse\x12J\n\x11VerifyDraftTokens\x12\x19.specdecode.VerifyRequest\x1a\x1a.specdecode.VerifyResponse\x12K\n\x0e\x46inalizeTokens\x12\x1b.specdecode.FinalizeRequest\x1a\x1c.specdecode.FinalizeResponse\x12\x46\n\x0cGenerateFull\x12\x18.specdecode.StartRequest\x1a\x1c.specdecode.GenerateResponseB\x03\x90\x01\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'inference_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\220\001\000'
  _globals['_STARTREQUEST']._serialized_start=31
  _globals['_STARTREQUEST']._serialized_end=120
  _globals['_STARTRESPONSE']._serialized_start=122
  _globals['_STARTRESPONSE']._serialized_end=159
  _globals['_DRAFTSEQUENCE']._serialized_start=161
  _globals['_DRAFTSEQUENCE']._serialized_end=239
  _globals['_VERIFYBATCHREQUEST']._serialized_start=241
  _globals['_VERIFYBATCHREQUEST']._serialized_end=307
  _globals['_VERIFYREQUEST']._serialized_start=309
  _globals['_VERIFYREQUEST']._serialized_end=387
  _globals['_VERIFYRESULT']._serialized_start=389
  _globals['_VERIFYRESULT']._serialized_end=488
  _globals['_VERIFYBATCHRESPONSE']._serialized_start=490
  _globals['_VERIFYBATCHRESPONSE']._serialized_end=554
  _globals['_FINALIZESEQUENCE']._serialized_start=556
  _globals['_FINALIZESEQUENCE']._serialized_end=610
  _globals['_FINALIZEBATCHREQUEST']._serialized_start=612
  _globals['_FINALIZEBATCHREQUEST']._serialized_end=683
  _globals['_FINALIZEBATCHRESULT']._serialized_start=685
  _globals['_FINALIZEBATCHRESULT']._serialized_end=744
  _globals['_FINALIZEBATCHRESPONSE']._serialized_start=746
  _globals['_FINALIZEBATCHRESPONSE']._serialized_end=819
  _globals['_VERIFYRESPONSE']._serialized_start=821
  _globals['_VERIFYRESPONSE']._serialized_end=902
  _globals['_FINALIZEREQUEST']._serialized_start=904
  _globals['_FINALIZEREQUEST']._serialized_end=991
  _globals['_FINALIZERESPONSE']._serialized_start=993
  _globals['_FINALIZERESPONSE']._serialized_end=1050
  _globals['_GENERATEREQUEST']._serialized_start=1052
  _globals['_GENERATEREQUEST']._serialized_end=1069
  _globals['_GENERATERESPONSE']._serialized_start=1071
  _globals['_GENERATERESPONSE']._serialized_end=1110
  _globals['_SPECULATIVESERVICE']._serialized_start=1113
  _globals['_SPECULATIVESERVICE']._serialized_end=1608
# @@protoc_insertion_point(module_scope)
