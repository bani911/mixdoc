# -*- coding: utf-8 -*-

from odoo import models, fields, api
import datetime

class gudang_arsip(models.Model):
    _name = 'gudang.arsip'

    company_id = fields.Many2one('res.company', 'Organisasi', default=lambda self: self.env.user.company_id, readonly=True)
    unit_kerja = fields.Many2one('jenis.unit', 'Unit_Kerja', required=True)
    name = fields.Char(string="Nama_Dok", required=True)
    no_dok = fields.Char(string="No.Dokumen", readonly=True)
    tahun = fields.Integer(string="Tahun", required=True)
    no_kotak = fields.Char(string="No.Kotak", required=True)
    masa_berlaku = fields.Integer(string="Masa Berlaku (thn)", required=True)
    tgl_masuk = fields.Date('Tgl Masuk Gudang', required=True)
    penerima = fields.Many2one('res.users', 'Penerima', required=True)
    keterangan = fields.Text('Keterangan')
    lampiran_dok = fields.Binary("Lampiran")
    doc_filename_dok = fields.Char("Filename Lampiran")
    penyerah_dok = fields.Many2one('res.users', 'Yg_Menyerahkan_Dok', required=True)
    tgl_terima = fields.Date('Tgl_Penyerahan_Dok', required=True)
    gudang = fields.Many2one('gudang', 'Gudang', required=True)
    no_gudang = fields.Char("No.Gudang")
    no_rak = fields.Char("No.Rak")


    def get_sequence(self, name=False, obj=False, pref=False, context=None):
        sequence_id = self.env['ir.sequence'].search([('name', '=', name), ('code', '=', obj), ('prefix', '=', pref)])
        if not sequence_id:
            sequence_id = self.env['ir.sequence'].sudo().create({
                'name': name,
                'code': obj,
                'implementation': 'no_gap',
                'prefix': '',
                'padding': 3
            })
        return sequence_id.next_by_id()

    @api.model
    def create(self, vals):
        # get kode organisasi session
        kode = self.env.user.company_id.kode
        a = self.get_sequence('Kode Nomor Gudang Arsip', 'gudang.arsip','')

        vals['no_dok'] = 'ARSIP-' + kode + '/' + datetime.date.today().strftime("%m") + '-' + datetime.date.today().strftime("%Y") + '/' + a
        return super(gudang_arsip, self).create(vals)